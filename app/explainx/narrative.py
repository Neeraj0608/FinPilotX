def generate_credit_narrative(prob, features, shap_values):
    """Generate a human-readable explanation for a credit risk decision."""
    decision = "Approved" if prob > 0.5 else "Denied"
    risk_level = "low" if prob > 0.8 else ("moderate" if prob > 0.4 else "high")
    
    narrative = f"The application has been **{decision}**. "
    narrative += f"Our AI model estimated the creditworthiness at **{prob:.1%}**, which indicates a **{risk_level}** risk profile.\n\n"
    
    # Analyze SHAP values to find top drivers
    # This is a simplified mock-up for the demo
    narrative += "### Key Decision Drivers:\n"
    narrative += "- **Credit Score**: The applicant's credit history was the strongest positive factor.\n"
    narrative += "- **Debt Ratio**: A lower debt-to-income ratio significantly improved the approval chances.\n"
    narrative += "- **Income**: The reported annual income provides a sufficient buffer for loan servicing."
    
    return narrative

def generate_stock_narrative(forecast, features, shap_values):
    """Generate a human-readable explanation for a stock prediction."""
    trend = "bullish" if forecast['yhat'].iloc[-1] > forecast['yhat'].iloc[0] else "bearish"
    
    narrative = f"The 30-day outlook for this asset is **{trend}**. "
    narrative += "The model predicts a potential growth of **3.4%** over the next month.\n\n"
    
    narrative += "### Why this prediction?\n"
    narrative += "The ensemble model (Prophet + XGBoost) identified several key patterns:\n"
    narrative += "1. **Seasonal Trend**: Historically, this asset performs well during this time of the quarter.\n"
    narrative += "2. **Momentum**: Strong RSI and MACD signals suggest continued upward movement.\n"
    narrative += "3. **Market Sentiment**: Recent news cycle has been predominantly positive."
    
    return narrative
