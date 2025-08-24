import streamlit as st
import requests
import json
from PIL import Image

# --- CONFIGURATION ---
# The URL of your deployed Render API
API_URL = "https://churn-prediction-api-rm3i.onrender.com/predict"

# Set a page configuration for a professional look
st.set_page_config(
    page_title="Churn Prediction Dashboard",
    page_icon="📈",
    layout="wide",
)

# --- HEADER & INTRODUCTION ---
# Use an image from a URL as the logo
icon_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSsEjCF4FN_y1bW3xk6FCul2HvhV3NTG51itQ&s"
st.image(icon_url, width=100)

st.title("📊 Customer Churn Prediction Dashboard")
st.markdown("---") # A horizontal line for separation

st.markdown(
    """
    This dashboard predicts whether a customer is likely to churn (leave the company) 
    based on their service usage and account information. 
    Simply enter the customer's data below and click 'Predict'.
    """
)
st.markdown("---")

# --- INPUT FORM & LOGIC ---
st.subheader("👤 Customer Profile")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        gender = st.selectbox("Gender", ["Female", "Male"])
        SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
        Partner = st.selectbox("Partner", ["Yes", "No"])
        Dependents = st.selectbox("Dependents", ["Yes", "No"])
        
    with col2:
        tenure = st.slider("Tenure (months)", 0, 72, 24)
        Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
        PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
        MultipleLines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])

    with col3:
        PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
        PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
        customerID = st.text_input("Customer ID", "12345")
        Tenure_Group = st.selectbox("Tenure Group", ["0-12", "13-24", "25-48", "49-60", "61-72"])

st.subheader("🌐 Service Usage")
with st.container():
    col4, col5, col6 = st.columns(3)
    with col4:
        InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
        OnlineSecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
        OnlineBackup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    with col5:
        DeviceProtection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
        TechSupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    with col6:
        StreamingTV = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
        StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    
st.subheader("💰 Billing Information")
with st.container():
    col7, col8 = st.columns(2)
    with col7:
        MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
    with col8:
        TotalCharges = st.number_input("Total Charges", min_value=0.0)

st.markdown("---")

# --- PREDICTION BUTTON & RESULT ---
if st.button("Predict Churn", type="primary"):
    with st.spinner('Predicting...'):
        # Prepare the JSON data payload from the user inputs
        data = {
            "gender": gender,
            "SeniorCitizen": SeniorCitizen,
            "Partner": Partner,
            "Dependents": Dependents,
            "tenure": tenure,
            "PhoneService": PhoneService,
            "MultipleLines": MultipleLines,
            "InternetService": InternetService,
            "OnlineSecurity": OnlineSecurity,
            "OnlineBackup": OnlineBackup,
            "DeviceProtection": DeviceProtection,
            "TechSupport": TechSupport,
            "StreamingTV": StreamingTV,
            "StreamingMovies": StreamingMovies,
            "Contract": Contract,
            "PaperlessBilling": PaperlessBilling,
            "PaymentMethod": PaymentMethod,
            "MonthlyCharges": MonthlyCharges,
            "TotalCharges": TotalCharges,
            "customerID": customerID,
            "Tenure_Group": Tenure_Group
        }
        
        # Send the POST request to the API
        response = requests.post(API_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
        
        # Process and display the result
        if response.status_code == 200:
            prediction = response.json()
            label = prediction['prediction_label']
            score = prediction['prediction_score']
            
            st.write("### Prediction Results")
            if label == "1":
                st.error(f"**Outcome:** The customer is predicted to **CHURN**")
                st.markdown(f"**Confidence Score:** {score*100:.2f}%")
                st.markdown("---")
                st.markdown("#### Actions Recommended:")
                st.write("Offer personalized incentives or a loyalty program to retain the customer.")
            else:
                st.success(f"**Outcome:** The customer is predicted to **NOT CHURN**")
                st.markdown(f"**Confidence Score:** {score*100:.2f}%")
                st.markdown("---")
                st.markdown("#### Actions Recommended:")
                st.write("Keep monitoring their activity and offer proactive customer service.")
        else:
            st.error(f"Error: Unable to get a prediction. Status code: {response.status_code}")
            st.json(response.json()) # Displaying the full error response for debugging