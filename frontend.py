import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("AI predictor")
st.markdown("``` Enter your details below: ```")


def _combine(vals):
    return "".join(chr(v) for v in vals)

# Input fields
age = st.number_input("Age", min_value=0, max_value=150, value=30)
weight = st.number_input("weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("height (meters)", min_value=0.1, max_value=2.5, value=1.5)
income_lpa = st.number_input("Income (LPA)", min_value=.01, value=12.0)
smoker = st.selectbox("Are you a smoker?", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    options=['retired', 'freelancer', 'student', 'government_job',
             'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict your insurance"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    
    response = requests.post(API_URL, json=input_data)

    if response.status_code == 200:
        result = response.json()

        if isinstance(result, dict) and 'predict_category' in result:
            st.success(f"Predicted Insurance: **{result['predict_category']}**")
        else:
            st.warning("Unexpected response format. Got: " + str(result))
    else:
        st.error(f"API call failed with status code: {response.status_code}")
