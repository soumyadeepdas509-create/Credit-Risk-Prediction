# Credit Risk Prediction

This project predicts the probability of loan default using machine learning on the Give Me Some Credit dataset.

## Dataset
Kaggle: Give Me Some Credit

150,000 customers with financial attributes.

## Features
- RevolvingUtilizationOfUnsecuredLines
- Age
- DebtRatio
- MonthlyIncome
- NumberOfOpenCreditLines
- Late Payment History

## Machine Learning Pipeline

1. Data Cleaning
2. Missing Value Handling
3. Exploratory Data Analysis
4. Feature Engineering
5. Handling Imbalanced Data (SMOTE)
6. Model Training

Models used:
- Logistic Regression
- Random Forest
- Gradient Boosting

## Model Evaluation

Metrics used:
- ROC AUC
- Precision Recall Curve
- Confusion Matrix

Best Model: Random Forest

ROC-AUC ≈ 0.95

## Explainability

SHAP was used to interpret model predictions.

## How to Run the Project

1. Clone the repository

git clone https://github.com/soumyadeepdas509-create/Credit-Risk-Prediction.git

2. Move into the project folder

cd Credit-Risk-Prediction

3. Install dependencies

pip install -r requirements.txt

4. Run the notebook

jupyter notebook credit_risk_prediction.ipynb
