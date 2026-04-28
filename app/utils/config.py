import os
from dotenv import load_dotenv

load_dotenv()

# App Settings
APP_NAME = "FinPilot X"
APP_ICON = "📈"
THEME_COLOR = "#00FFA3"

# API Keys
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "demo")

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'data', 'db', 'finpilotx.db')}")
CACHE_DIR = os.path.join(BASE_DIR, "..", ".model_cache")

# Model Settings
SENTIMENT_MODEL_NAME = "ProsusAI/finbert"
STOCK_PREDICTION_DAYS = 30
