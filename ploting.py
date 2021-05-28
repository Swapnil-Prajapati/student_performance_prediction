import streamlit as st
import pandas as pd
import plotly_express as px


def ploting():
    # configuration
    st.set_option('deprecation.showfileUploaderEncoding', False)

    # Title
    st.title("Data Visualization")
    # Sidebar
    st.sidebar.subheader("Data visualization settings")
    # File Upload
    uploaded_file = st.sidebar.file_uploader(
        label="Upload your CSV or Excel file",
        type=['csv', 'xlsx'])

    global df
    global numeric_columns
    if uploaded_file is not None:
        print(uploaded_file)

        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            print(e)
            df = pd.read_excel(uploaded_file)


    try:
        numeric_columns = list(df.select_dtypes(['float', 'int']).columns)
    except Exception as e:
        print(e)

    chart_select = st.sidebar.selectbox(
        label="select the chart type",
        options=['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
    )


    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Scatterplots Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.scatter(data_frame=df, x=x_values, y=y_values)
            st.plotly_chart(plot)
            x_select = st.sidebar.slider('X axis', x_values)
            y_select = st.sidebar.slider('Y axis', x_values)
        except Exception as e:
            print(e)

    if chart_select == 'Histogram':
        st.sidebar.subheader("Histogram Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.histogram(data_frame=df, x=x_values, y=y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Lineplots':
        st.sidebar.subheader("Lineplots Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.line(data_frame=df, x=x_values, y=y_values)
            st.plotly_chart(plot)

        except Exception as e:
            print(e)

    if chart_select == 'Boxplot':
        st.sidebar.subheader("Boxplot Settings")
        try:
            x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
            plot = px.box(data_frame=df, x=x_values, y=y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

