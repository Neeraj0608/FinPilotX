import pytest
import pandas as pd
from app.models.credit_model import CreditRiskModel
from app.models.sentiment_model import SentimentModel
from app.data.synthetic import generate_stock_data

def test_credit_model_prediction():
    model = CreditRiskModel()
    input_data = {
        "income": 50000, "age": 30, "loan_amount": 10000, 
        "credit_score": 700, "employment_years": 5, "debt_ratio": 0.3
    }
    decision, prob = model.predict(input_data)
    assert decision in ["Approved", "Denied"]
    assert 0 <= prob <= 1

def test_sentiment_model_fallback():
    model = SentimentModel()
    # Test fallback if transformers not loaded
    result = model.analyze("Test message")
    assert "label" in result
    assert "score" in result

def test_stock_data_generation():
    df = generate_stock_data("AAPL", days=10)
    assert len(df) == 10
    assert "Close" in df.columns
