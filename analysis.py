import pandas as pd

def correlation_analysis(df):

    numeric_df = df.select_dtypes(include='number')

    corr_matrix = numeric_df.corr()

    return corr_matrix
