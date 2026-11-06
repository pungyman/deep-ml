import pandas as pd

def solution(df):
    # drop columns with missing values greater than 0.5
    df = df.loc[:, df.isna().mean() <= 0.5]

    # drop rows with missing values greater than 0.5
    df = df.loc[df.isna().mean(axis=1) <= 0.5]

    # imputation
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode().iloc[0])
    
    return df.reset_index(drop=True)

    
    