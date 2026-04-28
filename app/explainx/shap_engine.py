import shap
import matplotlib.pyplot as plt
import streamlit as st

class ShapEngine:
    @staticmethod
    def get_waterfall_plot(model, X, sample_idx=0):
        """Generate a SHAP waterfall plot for a single prediction."""
        explainer = shap.TreeExplainer(model)
        shap_values = explainer(X)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        shap.plots.waterfall(shap_values[sample_idx], show=False)
        plt.tight_layout()
        return fig

    @staticmethod
    def get_summary_plot(model, X):
        """Generate a SHAP summary plot (beeswarm)."""
        explainer = shap.TreeExplainer(model)
        shap_values = explainer(X)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        shap.plots.beeswarm(shap_values, show=False)
        plt.tight_layout()
        return fig

    @staticmethod
    def get_feature_importance_plot(model, X):
        """Generate a SHAP feature importance bar plot."""
        explainer = shap.TreeExplainer(model)
        shap_values = explainer(X)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        shap.plots.bar(shap_values, show=False)
        plt.tight_layout()
        return fig
