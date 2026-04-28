import streamlit as st
import base64

def set_page_container_style():
    st.markdown(
        """
        <style>
        .main {
            background-color: #0E1117;
            color: #FAFAFA;
        }
        .stButton>button {
            width: 100%;
            border-radius: 5px;
            height: 3em;
            background-color: #00FFA3;
            color: #0E1117;
            font-weight: bold;
            border: none;
        }
        .stButton>button:hover {
            background-color: #00CC82;
            color: #0E1117;
        }
        /* Custom Cards */
        .metric-card {
            background-color: #1E2130;
            padding: 20px;
            border-radius: 10px;
            border-left: 5px solid #00FFA3;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def format_currency(value):
    return f"${value:,.2f}"

def format_percentage(value):
    return f"{value:.2f}%"
