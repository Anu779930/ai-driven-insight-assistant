from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    numeric_df = df.select_dtypes(include=['int64', 'float64'])

    if numeric_df.empty:
        print("[ANOMALY] No numeric columns found")
        df["anomaly"] = 0
        return df

    model = IsolationForest(contamination=0.1, random_state=42)
    df["anomaly"] = model.fit_predict(numeric_df)

    print("[ANOMALY] Detection completed")
    return df
