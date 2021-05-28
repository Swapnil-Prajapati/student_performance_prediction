import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import plotly_express as px

# Web App Title

# Upload CSV data


def run_eda():
    with st.sidebar.header('1. Upload your CSV data'):
        uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
        st.sidebar.markdown("""
    [Example CSV input file](https://github.com/Swapnil-Prajapati/Student_dataset/blob/main/exported-Stu-por1.csv)
    """)

    # Pandas Profiling Report
    if uploaded_file is not None:
        @st.cache
        def load_csv():
            csv = pd.read_csv(uploaded_file)
            return csv

        df = load_csv()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.write('---')
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
    else:
        st.info('Awaiting for CSV file to be uploaded.')
        if st.button('Press to use Example Dataset'):
            # Example data
            @st.cache
            def load_data():
                a = pd.DataFrame(
                    np.random.rand(100, 5),
                    columns=['a', 'b', 'c', 'd', 'e']
                )
                return a

            df = load_data()
            pr = ProfileReport(df, explorative=True)
            st.header('**Input DataFrame**')
            st.write(df)
            st.write('---')
            st.header('**Pandas Profiling Report**')
            st_profile_report(pr)



