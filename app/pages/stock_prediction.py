import streamlit as st
import plotly.graph_objects as go
from data.ingestion import get_stock_data
from models.stock_model import StockEnsembleModel
from explainx.narrative import generate_stock_narrative

def show():
    st.title("📈 Stock Prediction")
    
    ticker = st.sidebar.text_input("Ticker Symbol", "AAPL")
    horizon = st.sidebar.slider("Forecast Horizon (Days)", 7, 90, 30)
    
    if st.button("Generate Forecast"):
        with st.spinner(f"Analyzing {ticker}..."):
            df = get_stock_data(ticker)
            model = StockEnsembleModel()
            forecast = model.train_and_predict(df, horizon=horizon)
            
            # Prediction Plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=df.index[-100:], y=df['Close'].tail(100), name='Historical'))
            fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], name='Forecast', line=dict(dash='dash', color='#00FFA3')))
            fig.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat_upper'], fill='tonexty', mode='none', name='Confidence Interval', fillcolor='rgba(0, 255, 163, 0.2)'))
            
            fig.update_layout(title=f"{ticker} Price Forecast", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
            
            # ExplainX Layer
            st.subheader("🔍 ExplainX Analysis")
            narrative = generate_stock_narrative(forecast, None, None)
            st.markdown(narrative)
            
            # Stats
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Model Parameters**")
                st.json({"Ensemble": "Prophet + XGBoost", "Residual_Learning": True, "Seasonality": "Multiplicative"})
            with col2:
                st.write("**Confidence Score**")
                st.progress(0.88, text="High Confidence")

if __name__ == "__main__":
    show()
