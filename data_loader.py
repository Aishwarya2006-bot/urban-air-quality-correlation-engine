import streamlit as st
import pandas as pd
import numpy as np


@st.cache_data
def generate_synthetic_dataset():

    np.random.seed(42)

    periods = 30 * 24

    timestamps = pd.date_range(
        start="2025-01-01",
        periods=periods,
        freq="h"
    )

    traffic = np.random.normal(
        500,
        120,
        periods
    )

    traffic = np.clip(
        traffic,
        100,
        None
    )

    wind = np.random.normal(
        15,
        4,
        periods
    )

    wind = np.clip(
        wind,
        1,
        None
    )

    temp = np.random.normal(
        28,
        5,
        periods
    )

    pm25 = (
        0.08 * traffic
        - 0.7 * wind
        + 0.2 * temp
        + np.random.normal(
            0,
            5,
            periods
        )
    )

    no2 = (
        0.05 * traffic
        - 0.4 * wind
        + 0.1 * temp
        + np.random.normal(
            0,
            3,
            periods
        )
    )

    return pd.DataFrame({
        "Timestamp": timestamps,
        "PM2.5_Level": pm25,
        "NO2_Level": no2,
        "Traffic_Volume_Count": traffic,
        "Wind_Speed_kmh": wind,
        "Temperature_C": temp
    })


@st.cache_data
def load_dataset(
    uploaded_file=None,
    use_synthetic=False
):

    if use_synthetic:
        return generate_synthetic_dataset()

    try:

        if uploaded_file is not None:

            df = pd.read_csv(
                uploaded_file
            )

        else:

            df = pd.read_csv(
                "aqi_traffic_weather.csv"
            )

        df["Timestamp"] = pd.to_datetime(
            df["Timestamp"]
        )

        return df

    except Exception:

        st.info(
            "CSV not found. Using synthetic dataset."
        )

        return generate_synthetic_dataset()
