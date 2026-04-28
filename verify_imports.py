import sys
import os

# Simulate running from the root
root_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = os.path.join(root_dir, 'app')
sys.path.append(app_dir)

print(f"Checking imports with sys.path: {sys.path}")

try:
    import streamlit as st
    import pandas as pd
    import numpy as np
    from prophet import Prophet
    import xgboost as xgb
    import torch
    import transformers
    import sqlalchemy
    import shap
    print("Core dependencies OK")
except Exception as e:
    print(f"Dependency error: {e}")

try:
    from utils.config import APP_NAME
    from utils.db import init_db
    from models.stock_model import StockEnsembleModel
    from data.synthetic import generate_stock_data
    from explainx.narrative import generate_stock_narrative
    print("Project imports OK")
except Exception as e:
    print(f"Import error: {e}")
    import traceback
    traceback.print_exc()
