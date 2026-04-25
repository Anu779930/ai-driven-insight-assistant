import pandas as pd

def clean_data(df: pd.DataFrame):
    df = df.copy()

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Handle missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    print("[CLEANING] Data cleaned successfully")
    return df