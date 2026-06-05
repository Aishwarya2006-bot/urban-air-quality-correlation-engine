import streamlit as st
import pandas as pd
import plotly.express as px

from analysis import correlation_analysis

st.title("Urban Air Quality Correlation Engine")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    corr_matrix = correlation_analysis(df)

    st.subheader("Correlation Matrix")

    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        aspect="auto"
    )

    st.plotly_chart(fig)

    st.subheader("AQI Relationships")

    columns = df.select_dtypes(include='number').columns

    x_col = st.selectbox(
        "Select X Variable",
        columns
    )

    y_col = st.selectbox(
        "Select Y Variable",
        columns,
        index=1
    )

    scatter = px.scatter(
        df,
        x=x_col,
        y=y_col,
        trendline="ols"
    )

    st.plotly_chart(scatter)
