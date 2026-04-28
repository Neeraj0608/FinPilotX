import pandas as pd
import requests
from alpha_vantage.timeseries import TimeSeries
from data.synthetic import generate_stock_data, generate_news_headlines
from utils.config import ALPHA_VANTAGE_API_KEY
import streamlit as st

@st.cache_data
def get_stock_data(ticker):
    """Fetch stock or crypto data from Alpha Vantage or fallback to synthetic."""
    if ALPHA_VANTAGE_API_KEY == "demo":
        return generate_stock_data(ticker)
    
    try:
        # Check if it's a crypto ticker (e.g., BTC-USD)
        if '-' in ticker or any(x in ticker.upper() for x in ['BTC', 'ETH', 'SOL', 'DOGE']):
            # For Crypto, Alpha Vantage uses a different API structure
            symbol = ticker.split('-')[0]
            market = ticker.split('-')[1] if '-' in ticker else 'USD'
            url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={market}&apikey={ALPHA_VANTAGE_API_KEY}"
            r = requests.get(url)
            data_json = r.json()
            
            if "Time Series (Digital Currency Daily)" in data_json:
                raw_data = data_json["Time Series (Digital Currency Daily)"]
                df = pd.DataFrame.from_dict(raw_data, orient='index')
                
                # Identify columns more robustly by searching for keywords
                col_map = {}
                # Preferred order: Look for 'USD' or 'a.' versions first, then fall back to anything with the keyword
                keywords = ['open', 'high', 'low', 'close']
                for kw in keywords:
                    # Priority 1: contains keyword AND (usd or a.)
                    for col in df.columns:
                        c_low = col.lower()
                        if kw in c_low and ('(usd)' in c_low or 'a.' in c_low):
                            col_map[col] = kw.capitalize()
                            break
                    
                    # Priority 2: just contains the keyword (if not already found)
                    if kw.capitalize() not in col_map.values():
                        for col in df.columns:
                            if kw in col.lower():
                                col_map[col] = kw.capitalize()
                                break
                
                if len(col_map) >= 4:
                    df = df[list(col_map.keys())].rename(columns=col_map)
                    df = df[['Open', 'High', 'Low', 'Close']] # Ensure order
                    df.index = pd.to_datetime(df.index)
                    df = df.sort_index()
                    df.index.name = "Date"
                    return df.astype(float)
                else:
                    st.warning(f"Unexpected data format for {ticker}. Columns found: {list(df.columns)}")
                    return generate_stock_data(ticker)
            else:
                st.warning(f"No crypto data found for {ticker} in API response. Falling back to synthetic.")
                return generate_stock_data(ticker)

        # Standard Stock Logic
        ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')
        data, meta_data = ts.get_daily(symbol=ticker, outputsize='compact')
        # Rename columns to standard format
        data.columns = [col.split('. ')[1].capitalize() for col in data.columns]
        data.index.name = "Date"
        return data
    except Exception as e:
        st.warning(f"Error fetching data for {ticker}: {e}. Using synthetic data.")
        return generate_stock_data(ticker)

@st.cache_data
def get_news_data(ticker):
    """Fetch real-time news from Alpha Vantage News Sentiment API with strict filtering."""
    if ALPHA_VANTAGE_API_KEY == "demo":
        return generate_news_headlines(ticker)
    
    try:
        # Fetch a larger batch (50) to ensure we find relevant matches after filtering
        url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker}&limit=50&apikey={ALPHA_VANTAGE_API_KEY}"
        r = requests.get(url)
        data = r.json()
        
        if "Information" in data or "Note" in data:
            msg = data.get("Information") or data.get("Note")
            st.warning(f"Alpha Vantage Notice: {msg}")
            return generate_news_headlines(ticker)

        if "feed" in data:
            # Filter headlines locally to ensure the ticker is actually the focus
            # We check if the ticker symbol exists in the title or the item's ticker tags
            ticker_upper = ticker.upper()
            relevant_headlines = []
            
            for item in data['feed']:
                # Check title or tags
                has_ticker = ticker_upper in item.get('title', '').upper()
                ticker_tags = [t.get('ticker', '').upper() for t in item.get('ticker_sentiment', [])]
                
                if has_ticker or ticker_upper in ticker_tags:
                    relevant_headlines.append(item['title'])
                
                if len(relevant_headlines) >= 10:
                    break
            
            if not relevant_headlines:
                st.info(f"No specific news found for '{ticker}'. Showing general market news instead.")
                return [item['title'] for item in data['feed'][:10]]
                
            return relevant_headlines
        else:
            return generate_news_headlines(ticker)
    except Exception as e:
        st.error(f"Error fetching news for {ticker}: {e}")
        return generate_news_headlines(ticker)
