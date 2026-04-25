import pandas as pd

def load_data(file_path: str):
    df = pd.read_csv(file_path)
    print(f"[INGESTION] Loaded data shape: {df.shape}")
    return df