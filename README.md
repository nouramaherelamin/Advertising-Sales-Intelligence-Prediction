# Advertising Sales Intelligence & Prediction

An interactive Machine Learning and data analytics dashboard for understanding how advertising investments across **TV, Radio, and Newspaper** relate to **Sales**, with an interactive sales prediction tool powered by Linear Regression.

## 📊 Project Overview

This project transforms the Advertising dataset into an end-to-end analytics and machine learning application.

The dashboard provides:

- Advertising investment analysis
- Sales and channel relationship exploration
- Channel-level insights
- Interactive sales prediction
- Model performance evaluation
- Dataset exploration
- Data quality checks
- Interactive Plotly visualizations

## 🎯 Objectives

- Explore the relationship between advertising channels and sales.
- Identify how TV, Radio, and Newspaper spending relates to sales.
- Build a machine learning model for sales prediction.
- Evaluate model performance using standard regression metrics.
- Present the results through a professional Streamlit dashboard.

## 🗂️ Project Structure

```text
Advertising_Sales_Prediction/
│
├── app/
│   ├── app.py
│   └── assets/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── advertising_sales_model.joblib
│
├── notebooks/
├── reports/
├── src/
├── tests/
│
├── .streamlit/
│   └── config.toml
│
├── requirements.txt
├── README.md
├── SUBMISSION_CHECKLIST.md
└── .gitignore
```

## 🧠 Machine Learning

### Model

**Linear Regression**

The model uses:

- `TV`
- `Radio`
- `Newspaper`

to predict:

- `Sales`

### Dataset

- **200 observations**
- **3 advertising features**
- **1 target variable**

### Evaluation Metrics

| Metric | Result |
|---|---:|
| R² Score | 0.8994 |
| MAE | 1.4608 |
| RMSE | 1.7816 |

## 🖥️ Streamlit Dashboard

The application is organized into focused sections:

### Overview
A high-level view of the dataset, advertising channels, sales, and key project insights.

### Advertising Analysis
Explores advertising spending and its relationship with sales using interactive visualizations.

### Channel Insights
Provides channel-specific analysis for TV, Radio, and Newspaper advertising.

### Sales Predictor
Allows users to enter advertising budgets and generate a predicted sales value using the trained model.

### Model Performance
Displays regression evaluation metrics and model-related visualizations.

### Data Explorer
Provides an interactive view of the dataset and its main characteristics.

### Data Quality
Checks dataset structure and quality indicators.

## 🎨 Design

The dashboard uses a dark, modern analytics theme built around:

- Midnight Navy
- Electric Blue
- Cyan
- Neon Violet
- Emerald
- Amber
- Magenta

The interface includes responsive cards, interactive charts, navigation, custom assets, and Streamlit styling.

## 🛠️ Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit
- Joblib

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/nouramaherelamin/Advertising-Sales-Intelligence-Prediction.git
cd Advertising-Sales-Intelligence-Prediction
```

Install the required packages:

```bash
py -m pip install -r requirements.txt
```

## ▶️ Run the Dashboard

From the project root:

```bash
py -m streamlit run app/app.py
```

The application will open in your browser.

## 📈 Workflow

```text
Raw Data
   ↓
Data Cleaning
   ↓
Exploratory Data Analysis
   ↓
Feature & Target Selection
   ↓
Train/Test Split
   ↓
Linear Regression
   ↓
Model Evaluation
   ↓
Sales Prediction
   ↓
Interactive Streamlit Dashboard
```

## 📌 Key Features

- End-to-end data analysis workflow
- Machine learning regression model
- Interactive prediction interface
- Interactive Plotly charts
- Data quality inspection
- Model evaluation
- Professional dark UI
- Organized project structure
- GitHub-ready implementation

# 👩‍💻 Author
<div align="center">
  
**Noura Maher Elamin**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0A66C2?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/in/nouramaherelamin/)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/nouramaherelamin)
