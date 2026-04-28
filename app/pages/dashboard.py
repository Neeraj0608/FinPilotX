import streamlit as st
import plotly.express as px
from data.synthetic import generate_stock_data
from utils.helpers import format_currency

def show():
    st.title("📊 Financial Dashboard")
    
    # KPI Row
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Portfolio Value", format_currency(124500), "+5.2%")
    with col2:
        st.metric("Active Predictions", "14", "Running")
    with col3:
        st.metric("Average Model Accuracy", "88.4%", "+1.2%")

    st.markdown("---")
    
    # Main Chart
    st.subheader("Market Overview (S&P 500)")
    df = generate_stock_data("SPY", days=180)
    fig = px.line(df, x=df.index, y="Close", title="Historical Market Performance")
    fig.update_layout(template="plotly_dark", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

    # Bottom Row
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Recent Activity")
        st.table({
            "Module": ["Credit Risk", "Stock Pred", "Sentiment", "RL Trader"],
            "Asset/ID": ["USER_882", "AAPL", "NVDA News", "BTC Strategy"],
            "Status": ["Approved", "Bullish", "Positive", "Buy Signal"]
        })
    with c2:
        st.subheader("Model Health")
        st.progress(92, text="FinBERT Confidence")
        st.progress(85, text="Prophet Forecast Accuracy")
        st.progress(78, text="RL Agent Reward Growth")

if __name__ == "__main__":
    show()
