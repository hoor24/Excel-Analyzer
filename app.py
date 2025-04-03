import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit.components.v1 import html

def analyze_excel(file):
    try:
        df = pd.read_excel(file)
        profile = ProfileReport(df, explorative=True)
        return profile
    except Exception as e:
        st.error(f'Error processing file: {e}')
        return None

st.set_page_config(page_title='Excel Analyzer', page_icon='🌸', layout='wide')

page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to right, #ffdde1, #fff1f5);
    color: black;
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #ffdde1, #fff1f5);
    color: black;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🌸 Welcome to Excel Analyzer 🌸")
st.write("Upload your Excel file for instant analysis!")

uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

if uploaded_file:
    st.success('File upload successfully!')
    profile = analyze_excel(uploaded_file)
    if profile:
        report_html = profile.to_html()
        html(report_html, height=1000, scrolling=True)




