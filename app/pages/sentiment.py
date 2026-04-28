import streamlit as st
from models.sentiment_model import SentimentModel
from data.ingestion import get_news_data

def show():
    st.title("📰 Market Sentiment Analysis")
    
    ticker = st.text_input("Enter Ticker to Fetch Real-Time News", "AAPL")
    
    if st.button("Analyze Sentiment"):
        headlines = get_news_data(ticker)
        model = SentimentModel()
        
        with st.spinner("Running FinBERT..."):
            results = model.analyze_batch(headlines)
            
            # Aggregate stats
            labels = [r['label'] for r in results]
            avg_score = sum([r['score'] for r in results]) / len(results)
            
            # Overall Gauge
            st.subheader(f"Overall Sentiment: {max(set(labels), key=labels.count).upper()}")
            st.progress(avg_score, text=f"Confidence: {avg_score:.1%}")
            
            st.markdown("---")
            
            # Headline list
            for h, r in zip(headlines, results):
                color = "#00FFA3" if r['label'] == "positive" else ("#FF4B4B" if r['label'] == "negative" else "#888")
                st.markdown(f"""
                <div style="background-color: #1E2130; padding: 15px; margin-bottom: 10px; border-radius: 5px; border-right: 5px solid {color};">
                    <p style="margin: 0; font-weight: bold;">{h}</p>
                    <small style="color: {color};">Label: {r['label']} | Confidence: {r['score']:.1%}</small>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    show()
