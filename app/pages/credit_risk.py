import streamlit as st
from models.credit_model import CreditRiskModel
from explainx.shap_engine import ShapEngine
from explainx.narrative import generate_credit_narrative

def show():
    st.title("💳 Credit Risk Assessment")
    
    st.sidebar.header("Applicant Data")
    income = st.sidebar.number_input("Annual Income ($)", 20000, 500000, 75000)
    age = st.sidebar.number_input("Age", 18, 100, 35)
    loan = st.sidebar.number_input("Loan Amount ($)", 1000, 100000, 25000)
    credit_score = st.sidebar.slider("Credit Score", 300, 850, 720)
    emp_years = st.sidebar.number_input("Employment Years", 0, 50, 8)
    debt_ratio = st.sidebar.slider("Debt Ratio", 0.0, 1.0, 0.25)
    
    input_dict = {
        "income": income, "age": age, "loan_amount": loan, 
        "credit_score": credit_score, "employment_years": emp_years, "debt_ratio": debt_ratio
    }
    
    if st.button("Assess Risk"):
        model_obj = CreditRiskModel()
        decision, prob = model_obj.predict(input_dict)
        
        # Result Card
        color = "green" if decision == "Approved" else "red"
        st.markdown(f"""
        <div style="background-color: #1E2130; padding: 20px; border-radius: 10px; border-left: 10px solid {color};">
            <h2 style="color: white; margin-top: 0;">Decision: <span style="color: {color};">{decision}</span></h2>
            <p style="color: #FAFAFA; font-size: 1.2em;">Approval Probability: <b>{prob:.1%}</b></p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # ExplainX Layer
        st.subheader("🔍 Decision Interpretation (SHAP)")
        model, X_sample = model_obj.get_model_and_data()
        
        # Add the current input to sample for explanation
        import pandas as pd
        X_current = pd.DataFrame([input_dict])
        
        col1, col2 = st.columns([2, 1])
        with col1:
            fig = ShapEngine.get_waterfall_plot(model, X_current)
            st.pyplot(fig)
        with col2:
            narrative = generate_credit_narrative(prob, input_dict, None)
            st.markdown(narrative)

if __name__ == "__main__":
    show()
