import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_stock_data(ticker="AAPL", days=365):
    """Generate synthetic stock price data."""
    dates = pd.date_range(end=datetime.now(), periods=days)
    prices = [150.0]
    for _ in range(days - 1):
        prices.append(prices[-1] * (1 + np.random.normal(0.0005, 0.02)))
    
    df = pd.DataFrame({
        'Date': dates,
        'Open': prices,
        'High': [p * 1.01 for p in prices],
        'Low': [p * 0.99 for p in prices],
        'Close': prices,
        'Volume': np.random.randint(1000000, 5000000, size=days)
    })
    df.set_index('Date', inplace=True)
    return df

def generate_credit_data(n_samples=1000):
    """Generate synthetic credit application data for training."""
    data = {
        'income': np.random.normal(60000, 20000, n_samples),
        'age': np.random.randint(18, 80, n_samples),
        'loan_amount': np.random.normal(15000, 10000, n_samples),
        'credit_score': np.random.randint(300, 850, n_samples),
        'employment_years': np.random.randint(0, 40, n_samples),
        'debt_ratio': np.random.uniform(0.1, 0.6, n_samples)
    }
    df = pd.DataFrame(data)
    # Simple logic for target
    df['target'] = (df['credit_score'] > 600) & (df['income'] > 30000)
    df['target'] = df['target'].astype(int)
    return df

def generate_news_headlines(ticker="AAPL"):
    """Generate synthetic financial news headlines."""
    templates = [
        "{ticker} beats earnings expectations, stock surges.",
        "Analysts downgrade {ticker} following supply chain concerns.",
        "New product launch from {ticker} receives mixed reviews.",
        "{ticker} expansion into new markets shows promise.",
        "Regulatory hurdles could impact {ticker} growth in Q4."
    ]
    headlines = [t.format(ticker=ticker) for t in templates]
    return headlines
