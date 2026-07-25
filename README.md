# 💳 Credit Risk Prediction using Machine Learning

An end-to-end Machine Learning project that predicts the probability of customer loan default using the **Give Me Some Credit** dataset from Kaggle. The project includes data preprocessing, feature engineering, model comparison, evaluation, and deployment using **Streamlit**.

---

## 🌐 Live Demo

*🚀 Streamlit Web App:*  
https://credit-risk-prediction-j8jqhlugmrtoce2uqrp7ux.streamlit.app

---

## 📌 Project Overview

Financial institutions need to identify customers who are likely to default on loans. This project builds a supervised machine learning model to estimate the probability of financial distress based on customer financial information.

---

## 📊 Dataset

**Source:** Kaggle - Give Me Some Credit

- **Records:** 150,000 customers
- **Target Variable:** `SeriousDlqin2yrs`
- **Problem Type:** Binary Classification

---

## 🔧 Features Used

- RevolvingUtilizationOfUnsecuredLines
- Age
- NumberOfTime30-59DaysPastDueNotWorse
- DebtRatio
- MonthlyIncome
- NumberOfDependents
- CombinedDefaulted *(Feature Engineered)*
- CombinedCreditLoans *(Feature Engineered)*

---

## ⚙️ Project Workflow

1. Data Cleaning
2. Missing Value Treatment
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Selection
6. Model Training
7. Model Evaluation
8. Streamlit Deployment

---

## 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Random Forest
- **Gradient Boosting (Final Model)**

---

## 📈 Model Performance

| Model | Validation ROC-AUC |
|--------|-------------------:|
| Logistic Regression | 0.8103 |
| Random Forest | 0.8531 |
| **Gradient Boosting** | **0.8585** |

**Final Selected Model:** Gradient Boosting Classifier

---

## 📋 Evaluation Metrics

The models were evaluated using:

- ROC-AUC Score
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- Precision-Recall Curve
- Learning Curve
- Feature Importance

---

## 🚀 Deployment

The final Gradient Boosting model was saved as:

```
credit_risk_analysis_model.pkl
```

A **Streamlit** web application was developed where users can:

- Enter customer financial information
- Predict credit risk
- View the probability of default

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit

---

## 📁 Repository Structure

```
Credit-Risk-Prediction/
│── give_me_some_credit.ipynb
│── app.py
│── credit_risk_analysis_model.pkl
│── requirements.txt
│── README.md
│── LICENSE
```

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/soumyadeepdas509-create/Credit-Risk-Prediction.git
```

### 2. Move into the project folder

```bash
cd Credit-Risk-Prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit application

```bash
streamlit run app.py
```

### 5. (Optional) Open the notebook

```bash
jupyter notebook credit_risk_analysis_on_GiveMeSomeCredit_dataset.ipynb
```

---

## 🎯 Key Highlights

- End-to-end Machine Learning pipeline
- Feature Engineering
- Model Comparison
- Gradient Boosting Classifier
- ROC-AUC based evaluation
- Streamlit Deployment
- Financial Risk Prediction

---

## 👨‍💻 Author

**Soumyadeep Das**

If you found this project useful, consider giving the repository a ⭐.
