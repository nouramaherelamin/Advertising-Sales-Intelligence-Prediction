import pandas as pd
FEATURES=["TV","Radio","Newspaper"]
TARGET="Sales"
def load_data(path):
    df=pd.read_csv(path)
    if "Unnamed: 0" in df.columns: df=df.drop(columns=["Unnamed: 0"])
    df.columns=[c.strip() for c in df.columns]
    for c in FEATURES+[TARGET]: df[c]=pd.to_numeric(df[c],errors="coerce")
    return df.dropna().reset_index(drop=True)
