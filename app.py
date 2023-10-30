import streamlit as st
import pandas as pd
import pandas_dq

def generate_report(df):
    report = pandas_dq.dq_report(df)
    st.write(report)  # Adjust this line based on how pandas_dq structures the report

st.title('Data Report Generator')

uploaded_files = st.file_uploader("Choose CSV or Excel files", accept_multiple_files=True, type=['csv', 'xlsx'])

if uploaded_files:
    file_names = [file.name for file in uploaded_files]
    file_selection = st.selectbox("Select a file to analyze:", file_names)
    if st.button('Generate Report'):
        if file_selection.type == 'text/csv':
            df = pd.read_csv(file_selection)
        elif file_selection.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
            df = pd.read_excel(file_selection)
        generate_report(df)
