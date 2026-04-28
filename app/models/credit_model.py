import xgboost as xgb
import pandas as pd
from data.synthetic import generate_credit_data
from sklearn.model_selection import train_test_split

class CreditRiskModel:
    def __init__(self):
        self.model = None
        self.features = ['income', 'age', 'loan_amount', 'credit_score', 'employment_years', 'debt_ratio']

    def train(self):
        """Train the model on synthetic credit data."""
        df = generate_credit_data(n_samples=2000)
        X = df[self.features]
        y = df['target']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
        self.model.fit(X_train, y_train)
        return self.model

    def predict(self, input_dict):
        """Predict credit approval and risk score."""
        if self.model is None:
            self.train()
        
        df_input = pd.DataFrame([input_dict])
        prob = self.model.predict_proba(df_input[self.features])[0][1]
        decision = "Approved" if prob > 0.5 else "Denied"
        return decision, prob

    def get_model_and_data(self):
        """Return model and a sample dataset for SHAP explainer."""
        if self.model is None:
            self.train()
        df = generate_credit_data(n_samples=100)
        return self.model, df[self.features]
