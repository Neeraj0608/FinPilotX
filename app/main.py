import streamlit as st
import os
import sys

# Add the app directory to path to handle imports correctly
# This ensures that 'utils', 'models', etc. can be imported directly
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from utils.config import APP_NAME, APP_ICON
from utils.helpers import set_page_container_style
from utils.db import init_db

# Page Setup
st.set_page_config(
    page_title=APP_NAME,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# Initialize Database
init_db()

# Apply Custom Styling
set_page_container_style()

def main():
    st.sidebar.title(f"{APP_ICON} {APP_NAME}")
    st.sidebar.markdown("---")
    
    # Navigation is handled by Streamlit's multi-page directory structure (pages/)
    # But we can add a welcome message here
    st.title(f"Welcome to {APP_NAME}")
    st.markdown("""
    ### AI‑Powered Financial Decision Intelligence
    
    FinPilot X provides a transparent 'glass-box' approach to financial AI. 
    Select a module from the sidebar to get started:
    
    - **📊 Dashboard**: Portfolio overview and key metrics.
    - **📈 Stock Prediction**: Forecast asset prices with Prophet & XGBoost.
    - **💳 Credit Risk**: Assess loan applications with explainable AI.
    - **📰 Sentiment Analysis**: Analyze financial news with FinBERT.
    - **🤖 RL Trader**: Backtest automated trading strategies.
    - **🔍 ExplainX**: Deep-dive into model decision rationale.
    """)
    
    # Quick Stats Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.info("Market Sentiment: **Bullish**")
    with col2:
        st.success("Portfolio: **+12.4%**")
    with col3:
        st.warning("Risk Level: **Moderate**")
    with col4:
        st.error("Volatility: **High**")

if __name__ == "__main__":
    main()
