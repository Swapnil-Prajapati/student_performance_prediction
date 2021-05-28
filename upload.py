import streamlit as st
import plotly_express as px
import pandas as pd

global d


def upload_data():
    st.title("Upload your File")

    # setup of uploader
    uploded_file = st.file_uploader(label="Upload CSV or Excel file here.", type=['csv', 'xlsx'])

    global df
    if uploded_file is not None:
        print(uploded_file)
        print("hello")
        try:
            df = pd.read_csv(uploded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploded_file)

    #d = df
    st.write(df)
