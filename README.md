# Advertising Sales Prediction

End-to-end Machine Learning project for predicting **Sales** from advertising spend.

## Dataset
- Rows: 200
- Features: TV, Radio, Newspaper
- Target: Sales
- Problem: Supervised Regression
- Model: Linear Regression

## Test Results
- MAE: 1.4608
- MSE: 3.1741
- RMSE: 1.7816
- R²: 0.8994

## Structure
```text
Advertising_Sales_Prediction_Final/
├── app/
├── data/
│   ├── raw/
│   └── processed/
├── models/
├── notebooks/
├── reports/
├── src/
├── tests/
├── .streamlit/
├── requirements.txt
├── README.md
└── .gitignore
```

## Run
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m streamlit run app/app.py
```

## Retrain
```bash
python src/train_model.py
```

## Test
```bash
pytest -q
```

This project is for educational and analytical purposes; predictions are model estimates.
