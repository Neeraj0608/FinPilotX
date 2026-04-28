import pandas as pd
import numpy as np
from prophet import Prophet
import xgboost as xgb
from data.preprocessing import add_technical_indicators

class StockEnsembleModel:
    def __init__(self):
        self.prophet_model = None
        self.xgb_model = None

    def train_and_predict(self, df, horizon=30):
        """Train Prophet + XGBoost ensemble and predict future prices."""
        # 1. Prepare Prophet data
        df_reset = df.reset_index()
        # Find the date column (usually 'Date' or 'index') and 'Close'
        date_col = 'Date' if 'Date' in df_reset.columns else df_reset.columns[0]
        df_prophet = df_reset[[date_col, 'Close']].rename(columns={date_col: 'ds', 'Close': 'y'})
        self.prophet_model = Prophet(daily_seasonality=True)
        self.prophet_model.fit(df_prophet)
        
        future = self.prophet_model.make_future_dataframe(periods=horizon)
        forecast = self.prophet_model.predict(future)
        
        # 2. XGBoost for residuals (Simplified version for demo)
        # In a real app, we'd train on technical indicators
        df_features = add_technical_indicators(df)
        X = df_features.drop('Close', axis=1)
        y = df_features['Close']
        
        self.xgb_model = xgb.XGBRegressor(objective='reg:squarederror')
        self.xgb_model.fit(X, y)
        
        # Combine predictions (Simplified: just using Prophet for future)
        return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(horizon)

    def get_feature_importance(self, df):
        """Get XGBoost feature importance for SHAP."""
        df_features = add_technical_indicators(df)
        X = df_features.drop('Close', axis=1)
        return self.xgb_model, X
