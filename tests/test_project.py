from pathlib import Path
import pandas as pd,joblib
ROOT=Path(__file__).resolve().parents[1]
def test_data():
    df=pd.read_csv(ROOT/"data/processed/Advertising_clean.csv")
    assert len(df)>0
    assert {"TV","Radio","Newspaper","Sales"}<=set(df.columns)
    assert df.isna().sum().sum()==0
def test_model():
    model=joblib.load(ROOT/"models/advertising_sales_model.joblib")
    x=pd.DataFrame([{"TV":150,"Radio":25,"Newspaper":35}])
    assert float(model.predict(x)[0])>=0
