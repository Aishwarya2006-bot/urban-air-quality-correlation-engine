import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include=np.number
    )

    corr = numeric_df.corr()

    fig, ax = plt.subplots(
        figsize=(8,6)
    )

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        ax=ax
    )

    return fig


def scatter_with_trendline(
    df,
    x,
    y
):

    fig, ax = plt.subplots(
        figsize=(8,5)
    )

    sns.regplot(
        data=df,
        x=x,
        y=y,
        ax=ax
    )

    return fig
