# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 10:18:29 2025

@author: palak
"""

import pickle
import streamlit as st

# Load the saved model
placement_model = pickle.load(open('C:/internship/sav/placement_data.sav', 'rb'))

# Streamlit page configuration
st.set_page_config(page_title="Student Placement Predictor")
st.title("Student Placement Prediction App")
st.markdown("### Predict whether a student will be placed or not based on academic and personal details.")

# Input form layout
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    ssc_p = st.slider("SSC % (10th Grade)", 0.0, 100.0, 75.0)
    ssc_b = st.selectbox("SSC Board", ["Central", "Others"])
    hsc_p = st.slider("HSC % (12th Grade)", 0.0, 100.0, 70.0)
    hsc_b = st.selectbox("HSC Board", ["Central", "Others"])

with col2:
    hsc_s = st.selectbox("HSC Stream", ["Commerce", "Science", "Arts"])
    degree_p = st.slider("Degree %", 0.0, 100.0, 60.0)
    degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
    workex = st.selectbox("Work Experience", ["Yes", "No"])
    etest_p = st.slider("Employability Test %", 0.0, 100.0, 50.0)

with col3:
    specialisation = st.selectbox("MBA Specialization", ["Mkt&HR", "Mkt&Fin"])
    mba_p = st.slider("MBA %", 0.0, 100.0, 65.0)
    salary = st.number_input("Expected Salary (₹)", min_value=0.0, value=0.0)
    status = st.selectbox("Placement Status (Training only)", ["Placed", "Not Placed"])

# Encode categorical variables
gender_encoded = 1 if gender == "Male" else 0
ssc_b_encoded = 1 if ssc_b == "Central" else 0
hsc_b_encoded = 1 if hsc_b == "Central" else 0
hsc_s_encoded = {"Commerce": 0, "Science": 1, "Arts": 2}[hsc_s]
degree_t_encoded = {"Sci&Tech": 0, "Comm&Mgmt": 1, "Others": 2}[degree_t]
workex_encoded = 1 if workex == "Yes" else 0
specialisation_encoded = 1 if specialisation == "Mkt&Fin" else 0
status_encoded = 1 if status == "Placed" else 0

# Button for prediction
if st.button("Predict Placement Status"):
    input_data = [[
        gender_encoded, ssc_p, ssc_b_encoded, hsc_p, hsc_b_encoded,
        hsc_s_encoded, degree_p, degree_t_encoded, workex_encoded,
        etest_p, specialisation_encoded, mba_p, salary, status_encoded
    ]]
    
    try:
        prediction = placement_model.predict(input_data)
        result = "Placed ✅" if prediction[0] == 1 else "Not Placed ❌"
        st.success(f"Prediction: {result}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.markdown("*Note: This prediction is based on historical data and does not guarantee placement outcomes.*")
