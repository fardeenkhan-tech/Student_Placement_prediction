import streamlit as St
import pandas as pd
import joblib

# Load trained pipeline model
model = joblib.load("model.pkl")

St.title("🎓 Student Placement Prediction App")

St.sidebar.header("Enter Student Details")

# User Inputs
age = St.sidebar.slider("Age", 18, 30, 22)
cgpa = St.sidebar.slider("CGPA", 0.0, 10.0, 7.0)

internship = St.sidebar.slider("Internships", 0, 10, 1)
projects = St.sidebar.slider("Projects", 0, 10, 2)
certifications = St.sidebar.slider("Certifications", 0, 10, 1)

coding = St.sidebar.slider("Coding Skill", 0, 100, 60)
communication = St.sidebar.slider("Communication Skill", 0, 100, 60)
soft = St.sidebar.slider("Soft Skills", 0, 100, 60)

gender = St.sidebar.selectbox("Gender", ["Male", "Female"])
branch = St.sidebar.selectbox("Branch", ["CSE", "IT", "ECE", "MECH", "CIVIL"])
hackathon = St.sidebar.selectbox("Hackathon Participation", ["Yes", "No"])

# Create DataFrame
input_data = pd.DataFrame({
    "age":[age],
    "gender":[gender],
    "branch":[branch],
    "cgpa":[cgpa],
    "internship_count":[internship],
    "project_count":[projects],
    "certifications_count":[certifications],
    "coding_skills_score":[coding],
    "communication_skills_score":[communication],
    "soft_skills_score":[soft],
    "hackathon_participation":[hackathon]
})

St.subheader("Input Data")
St.write(input_data)

# Prediction
if St.button("Predict Placement"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        St.success("✅ Student is likely to be Placed")
    else:
        St.error("❌ Student is not likely to be Placed")