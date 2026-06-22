import streamlit as st
import pandas as pd
import joblib

model = joblib.load("knn_heart.pkl")
scaler = joblib.load("scaler (1).pkl")
columns = joblib.load("columns.pkl")


st.title("❤️ Heart Disease Prediction")
st.write("Provide the following details:")

age = st.slider("Age", 18, 100, 40)

sex = st.selectbox("Sex",["M", "F"])
chest_pain = st.selectbox("Chest Pain Type",["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)",min_value=80,max_value=250, value=120)

cholesterol = st.number_input("Cholesterol (mg/dL)",min_value=0,max_value=700,value=200)

fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0, 1])

max_hr = st.slider("Maximum Heart Rate",60,220,150)

exercise_angina = st.selectbox("Exercise Induced Angina",["Y", "N"])

resting_ecg = st.selectbox("Resting ECG",["Normal", "ST", "LVH"])

oldpeak = st.slider("Oldpeak (ST Depression)",0.0,6.0,1.0)


if st.button("Predict"):


    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,
        f"Sex_{sex}": 1,
        f"ChestPainType_{chest_pain}": 1,
        f"RestingECG_{resting_ecg}": 1,
        f"ExerciseAngina_{exercise_angina}": 1
    }


    input_df = pd.DataFrame([raw_input])


    for col in columns:
        if col not in input_df.columns:
            input_df[col] = 0


    input_df = input_df[columns]


    scaled_input = scaler.transform(input_df)


    prediction = model.predict(scaled_input)[0]


    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")