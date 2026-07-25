import streamlit as st
import joblib
import pandas as pd

# -----------------------
# Load Model
# -----------------------
artifact = joblib.load("credit_risk_analysis_model.pkl")

model = artifact["model"]
features = artifact["features"]

st.set_page_config(page_title="Credit Risk Prediction", page_icon="💳")

st.title("💳 Credit Risk Prediction")
st.write("Predict the probability of financial distress.")

# -----------------------
# Inputs
# -----------------------

revolving = st.number_input(
    "RevolvingUtilizationOfUnsecuredLines",
    min_value=0.0,
    value=0.50
)

age = st.number_input(
    "age",
    min_value=18,
    value=35
)

late30 = st.number_input(
    "NumberOfTime30-59DaysPastDueNotWorse",
    min_value=0,
    value=0
)

debt = st.number_input(
    "DebtRatio",
    min_value=0.0,
    value=0.50
)

income = st.number_input(
    "MonthlyIncome",
    min_value=0.0,
    value=5000.0
)

open_credit = st.number_input(
    "NumberOfOpenCreditLinesAndLoans",
    min_value=0,
    value=5
)

late90 = st.number_input(
    "NumberOfTimes90DaysLate",
    min_value=0,
    value=0
)

real_estate = st.number_input(
    "NumberRealEstateLoansOrLines",
    min_value=0,
    value=1
)

late60 = st.number_input(
    "NumberOfTime60-89DaysPastDueNotWorse",
    min_value=0,
    value=0
)

dependents = st.number_input(
    "NumberOfDependents",
    min_value=0.0,
    value=1.0
)


if st.button("Predict"):

    # Feature Engineering
    combined_default = late30 + late60 + late90
    combined_default = 1 if combined_default >= 1 else 0

    combined_credit = open_credit + real_estate
    combined_credit = 1 if combined_credit >= 5 else 0

    sample = pd.DataFrame([{
        "RevolvingUtilizationOfUnsecuredLines": revolving,
        "age": age,
        "NumberOfTime30-59DaysPastDueNotWorse": late30,
        "DebtRatio": debt,
        "MonthlyIncome": income,
        "NumberOfDependents": dependents,
        "CombinedDefaulted": combined_default,
        "CombinedCreditLoans": combined_credit
    }])

    sample = sample[features]

    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠ High Credit Risk")
    else:
        st.success("✅ Low Credit Risk")

    st.write(f"**Probability of Default:** {probability:.2%}")