# 🧠 Sales Prediction using Machine Learning

This project focuses on predicting product sales based on advertising spend across three channels: **TV**, **Radio**, and **Newspaper**. It uses regression models to forecast sales and includes a Streamlit web app for interactive predictions.

---

## 📊 Project Overview

Sales prediction is a critical task for marketing and business strategy. By leveraging machine learning, businesses can estimate future sales based on advertising investments. This project:

- Analyzes relationships between advertising media and product sales.
- Builds regression models to forecast sales.
- Evaluates model performance.
- Deploys an interactive prediction tool using Streamlit.

---

## 🧱 Dataset

The dataset used is **Advertising.csv**, containing the following columns:

| Feature     | Description                         |
|-------------|-------------------------------------|
| `TV`        | Advertising spend on TV campaigns   |
| `Radio`     | Advertising spend on radio          |
| `Newspaper` | Advertising spend on newspapers     |
| `Sales`     | Units of product sold               |

---

## 🛠️ Features & Workflow

### 🔍 Data Analysis & Preprocessing
- Visualized correlation between features and target variable.
- Checked for multicollinearity and dropped weak features (optional experiment).

### 🧪 Model Training
Trained and evaluated the following regression models:
- Linear Regression
- Random Forest Regressor
- XGBoost Regressor

### ✅ Model Evaluation Metrics
- R² Score
- Cross-validation scores
- Residual plots

### 📈 Feature Importance
- Feature impact measured using tree-based models (Random Forest & XGBoost).

---

## 🚀 Streamlit Web App

### 🎯 Features
- User inputs advertising spend.
- Predicts expected sales.
- Deployed using Streamlit interface.

### 🏗 App Structure

