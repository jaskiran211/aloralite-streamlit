import streamlit as st
import pandas as pd

st.set_page_config(page_title="AloraLite", layout="wide")

st.title("🏥 AloraLite – Home Healthcare CRM (Prototype)")

# Load data
patients = pd.read_csv("patients.csv")
caregivers = pd.read_csv("caregivers.csv")
visits = pd.read_csv("visits.csv")
ai = pd.read_csv("ai_suggestions.csv")

# Navigation menu
menu = st.sidebar.radio("Navigate", ["Patients", "Caregivers", "Visits", "AI Suggestions"])

if menu == "Patients":
    st.header("👩‍⚕️ Patients")
    st.dataframe(patients)

elif menu == "Caregivers":
    st.header("🧑‍⚕️ Caregivers")
    st.dataframe(caregivers)

elif menu == "Visits":
    st.header("📅 Visit Log")
    st.dataframe(visits)

elif menu == "AI Suggestions":
    st.header("🤖 AI-Powered Care Suggestions")
    selected_patient = st.selectbox("Select a patient:", ai["PatientName"].unique())
    suggestion = ai[ai["PatientName"] == selected_patient]["AI_Recommendation"].values[0]
    condition = ai[ai["PatientName"] == selected_patient]["Condition"].values[0]

    st.markdown(f"**Condition:** {condition}")
    st.markdown(f"**AI Recommendation:**")
    st.write(suggestion)
