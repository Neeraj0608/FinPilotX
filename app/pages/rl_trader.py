import streamlit as st
import plotly.graph_objects as go
from data.ingestion import get_stock_data
from models.rl_model import RLTrader

def show():
    st.title("🤖 Reinforcement Learning Trader")
    
    ticker = st.sidebar.text_input("Asset to Backtest", "BTC-USD")
    capital = st.sidebar.number_input("Initial Capital ($)", 1000, 100000, 10000)
    
    if st.button("Execute Strategy"):
        with st.spinner("Training RL Agent (PPO)..."):
            df = get_stock_data(ticker)
            trader = RLTrader()
            actions = trader.predict(df)
            
            # Simple Backtest calculation
            equity = [capital]
            for i, action in enumerate(actions):
                # 1: Buy, 2: Sell, 0: Hold
                change = (df['Close'].iloc[i+1] / df['Close'].iloc[i]) - 1 if i < len(df)-1 else 0
                if action == 1:
                    equity.append(equity[-1] * (1 + change))
                else:
                    equity.append(equity[-1])
            
            # Plot
            fig = go.Figure()
            fig.add_trace(go.Scatter(y=equity, name='RL Strategy Equity', line=dict(color='#00FFA3')))
            fig.update_layout(title=f"Equity Curve - {ticker}", template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)
            
            # Stats
            total_return = (equity[-1] / equity[0]) - 1
            st.metric("Total Return", f"{total_return:.2%}", delta=f"{total_return*100:.1f}% vs Benchmark")
            
            with st.expander("Strategy Logs"):
                st.write(f"Total Steps: {len(actions)}")
                st.write(f"Final Value: ${equity[-1]:,.2f}")

if __name__ == "__main__":
    show()
