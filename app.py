import streamlit as st
import pandas as pd

from src.data_loader import load_dataset
from src.analysis import (
    traffic_pm25_correlations,
    lag_analysis,
    weather_significance
)
from src.visualizations import (
    correlation_heatmap,
    scatter_with_trendline
)

st.set_page_config(
    page_title="Urban Air Quality Correlation Engine",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Urban Air Quality Correlation Engine")

st.markdown("""
Analyze how traffic and weather influence urban air pollution.
""")

# =====================================
# SIDEBAR
# =====================================

st.sidebar.header("Dataset Controls")

uploaded_file = st.sidebar.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

use_synthetic = st.sidebar.toggle(
    "Use Preloaded Synthetic Dataset"
)

# =====================================
# LOAD DATA
# =====================================

df = load_dataset(
    uploaded_file=uploaded_file,
    use_synthetic=use_synthetic
)

# =====================================
# OVERVIEW
# =====================================

st.subheader("Dataset Preview")

col1, col2, col3 = st.columns(3)

col1.metric("Rows", len(df))
col2.metric("Columns", len(df.columns))
col3.metric(
    "Variables",
    len(df.select_dtypes("number").columns)
)

st.dataframe(df.head())

# =====================================
# TABS
# =====================================

tab1, tab2, tab3 = st.tabs([
    "Correlation Matrix",
    "Bivariate Analysis",
    "Lag & Significance"
])

# =====================================
# TAB 1
# =====================================

with tab1:

    st.subheader("Correlation Matrix")

    fig = correlation_heatmap(df)

    st.pyplot(fig)

# =====================================
# TAB 2
# =====================================

with tab2:

    st.subheader("Interactive Scatter Plot")

    variables = [
        "PM2.5_Level",
        "NO2_Level",
        "Traffic_Volume_Count",
        "Wind_Speed_kmh",
        "Temperature_C"
    ]

    x = st.selectbox("X Variable", variables)

    y = st.selectbox(
        "Y Variable",
        variables,
        index=1
    )

    fig = scatter_with_trendline(df, x, y)

    st.pyplot(fig)

# =====================================
# TAB 3
# =====================================

with tab3:

    st.subheader("Traffic → PM2.5 Correlations")

    corr = traffic_pm25_correlations(df)

    c1, c2 = st.columns(2)

    c1.metric(
        "Pearson r",
        f"{corr['pearson_r']:.4f}"
    )

    c2.metric(
        "Spearman ρ",
        f"{corr['spearman_rho']:.4f}"
    )

    st.markdown("---")

    st.subheader("Lag Analysis")

    lag_df = lag_analysis(df)

    st.dataframe(
        lag_df,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Weather Impact Significance"
    )

    sig_df = weather_significance(df)

    st.dataframe(
        sig_df,
        use_container_width=True
    )
