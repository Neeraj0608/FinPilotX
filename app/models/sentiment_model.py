from transformers import pipeline
import torch
import streamlit as st

class SentimentModel:
    def __init__(self):
        self.model_name = "ProsusAI/finbert"
        self.pipe = None

    def load(self):
        """Load the FinBERT pipeline (with caching)."""
        if self.pipe is None:
            try:
                # Use CPU for demo if GPU not available
                device = 0 if torch.cuda.is_available() else -1
                self.pipe = pipeline("sentiment-analysis", model=self.model_name, device=device)
            except Exception as e:
                st.error(f"Failed to load FinBERT: {e}")
                return None
        return self.pipe

    def analyze(self, text):
        """Analyze text sentiment."""
        if self.pipe is None:
            self.load()
        
        if self.pipe:
            results = self.pipe(text)
            return results[0]
        else:
            # Fallback mock sentiment
            return {"label": "neutral", "score": 0.5}

    def analyze_batch(self, texts):
        """Analyze a list of texts."""
        if not texts:
            return []
            
        if self.pipe is None:
            self.load()
        if self.pipe:
            return self.pipe(texts)
        return [{"label": "neutral", "score": 0.5} for _ in texts]
