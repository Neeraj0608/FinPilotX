import streamlit as st
from explainx.visualizations import create_radar_chart, create_network_graph

def show():
    st.title("🔍 ExplainX Central")
    st.markdown("Global interpretability dashboard for all FinPilot X models.")
    
    tab1, tab2, tab3 = st.tabs(["Feature Correlations", "Global Risk Profile", "Model Insights"])
    
    with tab1:
        st.subheader("Global Feature Network")
        fig = create_network_graph()
        st.plotly_chart(fig, use_container_width=True)
        st.info("Nodes represent features; edges represent correlation strength detected by the ensemble model.")
        
    with tab2:
        st.subheader("Multi-Factor Risk Radar")
        categories = ['Market Volatility', 'Credit Exposure', 'Sentiment Bias', 'Operational Risk', 'Liquidity']
        values = [0.4, 0.2, 0.7, 0.3, 0.1]
        fig = create_radar_chart(categories, values, "Current Portfolio Risk Vector")
        st.plotly_chart(fig, use_container_width=True)
        
    with tab3:
        st.subheader("Explainable AI (XAI) Methods")
        st.markdown("""
        FinPilot X utilizes several SOTA interpretability techniques:
        
        - **SHAP (Shapley Additive Explanations)**: Unified measure of feature importance.
        - **FinBERT Attention**: Visualizing which tokens the transformer focuses on.
        - **Counterfactuals**: Simulating 'what-if' scenarios for credit approval.
        - **Narrative Generation**: LLM-driven human-readable justifications.
        """)

if __name__ == "__main__":
    show()
