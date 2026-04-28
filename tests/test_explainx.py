from app.explainx.narrative import generate_credit_narrative, generate_stock_narrative
import pandas as pd

def test_credit_narrative_generation():
    narrative = generate_credit_narrative(0.8, {}, None)
    assert "Approved" in narrative
    assert "80.0%" in narrative

def test_stock_narrative_generation():
    forecast = pd.DataFrame({'ds': [1, 2], 'yhat': [100, 110]})
    narrative = generate_stock_narrative(forecast, None, None)
    assert "bullish" in narrative
