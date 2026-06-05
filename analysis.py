import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import spearmanr


def traffic_pm25_correlations(df):

    pearson_r, pearson_p = pearsonr(
        df["Traffic_Volume_Count"],
        df["PM2.5_Level"]
    )

    spearman_rho, spearman_p = spearmanr(
        df["Traffic_Volume_Count"],
        df["PM2.5_Level"]
    )

    return {
        "pearson_r": pearson_r,
        "pearson_p": pearson_p,
        "spearman_rho": spearman_rho,
        "spearman_p": spearman_p
    }


def lag_analysis(df):

    temp = df.copy()

    temp["Traffic_Lag_1h"] = temp[
        "Traffic_Volume_Count"
    ].shift(1)

    temp["Traffic_Lag_2h"] = temp[
        "Traffic_Volume_Count"
    ].shift(2)

    output = []

    for label, col in {
        "0 Hour":"Traffic_Volume_Count",
        "1 Hour":"Traffic_Lag_1h",
        "2 Hour":"Traffic_Lag_2h"
    }.items():

        d = temp[
            [col, "PM2.5_Level"]
        ].dropna()

        r, p = pearsonr(
            d[col],
            d["PM2.5_Level"]
        )

        output.append([
            label,
            round(r,4),
            round(p,6),
            "Statistically Significant"
            if p < 0.05
            else "Not Significant"
        ])

    return pd.DataFrame(
        output,
        columns=[
            "Lag",
            "Correlation",
            "P Value",
            "Significance"
        ]
    )


def weather_significance(df):

    tests = [
        ("Wind_Speed_kmh",
         "PM2.5_Level"),

        ("Wind_Speed_kmh",
         "NO2_Level"),

        ("Temperature_C",
         "PM2.5_Level"),

        ("Temperature_C",
         "NO2_Level")
    ]

    output = []

    for x, y in tests:

        r, p = pearsonr(
            df[x],
            df[y]
        )

        output.append([
            x,
            y,
            round(r,4),
            round(p,6),
            "Statistically Significant"
            if p < 0.05
            else "Not Significant"
        ])

    return pd.DataFrame(
        output,
        columns=[
            "Variable",
            "Target",
            "Correlation",
            "P Value",
            "Significance"
        ]
    )
