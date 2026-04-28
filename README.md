# FinPilot X 🚀

AI‑powered financial decision intelligence platform with a "glass-box" interpretability layer.

## 🌟 Features

- **Stock Prediction**: Ensemble forecasting using Prophet and XGBoost.
- **Credit Risk Assessment**: Explainable loan approval scoring with SHAP waterfall charts.
- **Market Sentiment**: Real-time news analysis using FinBERT transformers.
- **RL Trader**: Automated strategy backtesting with PPO reinforcement learning.
- **ExplainX Layer**: Unified interpretability hub with natural language justifications.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **ML Models**: Scikit-Learn, XGBoost, Prophet, PyTorch, Transformers, Stable-Baselines3
- **Interpretability**: SHAP, NetworkX
- **Data**: Alpha Vantage API (with synthetic fallbacks)
- **Database**: SQLite (SQLAlchemy)
- **DevOps**: Docker, Docker Compose

## 🚀 Quick Start

1. **Clone the repository** (if applicable)
2. **Setup environment**:
   ```bash
   cp .env.example .env
   # Add your Alpha Vantage key or leave as 'demo'
   ```
3. **Run with Docker**:
   ```bash
   docker-compose up --build
   ```
4. **Access the app**:
   Open `http://localhost:8501` in your browser.

## 📂 Project Structure

- `app/main.py`: Entry point and navigation.
- `app/pages/`: Individual module UIs.
- `app/models/`: ML model logic and training.
- `app/explainx/`: Interpretability engines and visualizations.
- `app/data/`: Ingestion, preprocessing, and synthetic generators.
- `tests/`: Unit testing suite.
