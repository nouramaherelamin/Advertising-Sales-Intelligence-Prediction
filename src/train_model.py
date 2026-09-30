from pathlib import Path
import joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from data_preprocessing import load_data
ROOT=Path(__file__).resolve().parents[1]
df=load_data(ROOT/"data/processed/Advertising_clean.csv")
X=df[["TV","Radio","Newspaper"]]; y=df["Sales"]
Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.2,random_state=42)
model=Pipeline([("imputer",SimpleImputer(strategy="median")),("model",LinearRegression())])
model.fit(Xtr,ytr); p=model.predict(Xte)
print("MAE:",mean_absolute_error(yte,p))
print("RMSE:",mean_squared_error(yte,p)**.5)
print("R2:",r2_score(yte,p))
joblib.dump(model,ROOT/"models/advertising_sales_model.joblib")
