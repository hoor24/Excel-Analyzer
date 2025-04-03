import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

st.set_page_config(page_title="Excel Analyzer", page_icon="📊", layout="wide")
st.markdown(
    """
    <style>
        body {
            background-color: #0a0a0a;
            color: white;
            font-family: Arial, sans-serif;
        }
        .stApp {
            background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.2);
        }
        h1 {
            color: #8a2be2;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1>Hello! Upload Your Excel File 📊</h1>", unsafe_allow_html=True)


uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls", "csv"],
                                 help="Only Excel files are allowed.")

if uploaded_file is not None:
    try:

        df = pd.read_excel(uploaded_file)
        profile = ProfileReport(df, explorative=True)


        st_profile_report(profile)
    except Exception as e:
        st.error(f"Error processing the file: {e}")
