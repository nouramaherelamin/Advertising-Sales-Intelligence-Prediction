from pathlib import Path
import joblib, pandas as pd
ROOT=Path(__file__).resolve().parents[1]
MODEL_PATH=ROOT/"models"/"advertising_sales_model.joblib"
def predict_sales(tv,radio,newspaper):
    model=joblib.load(MODEL_PATH)
    x=pd.DataFrame([{"TV":tv,"Radio":radio,"Newspaper":newspaper}])
    return float(model.predict(x)[0])
