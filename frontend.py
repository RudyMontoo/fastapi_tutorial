import streamlit as st
import requests

st.title("Insurance Premium Predictor")

# ---- User Inputs ----
age = st.number_input("Age", min_value=1, max_value=120)
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (meters)", min_value=0.5, max_value=2.5)
income_lpa = st.number_input("Income (LPA)", min_value=0.1)
smoker = st.selectbox("Smoker", [True, False])
city = st.text_input("City")
occupation = st.selectbox(
    "Occupation",
    [
        "retired",
        "freelancer",
        "student",
        "government_job",
        "business_owner",
        "unemployed",
        "private_job",
    ],
)

# ---- API Call ----
if st.button("Predict Premium Category"):
    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation,
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Category: {result['predicted_category']}")
        else:
            st.error(f"Error: {response.text}")

    except Exception as e:
        st.error(f"API not reachable: {e}")