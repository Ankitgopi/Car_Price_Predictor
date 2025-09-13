import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model and encoders
try:
    model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
    with open('label_encoders.pkl', 'rb') as f:
        encoders = pickle.load(f)
    car = pd.read_csv('Cleaned_Car_data.csv')
except FileNotFoundError:
    st.error("Model files not found. Please run train_model.py first.")
    model = None
    encoders = None
    car = None

# Streamlit UI
st.title("🚗 Car Price Prediction App")

if car is not None and model is not None and encoders is not None:
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    # Dropdowns and inputs
    company = st.selectbox("Select Company", companies)
    car_model = st.selectbox("Select Car Model", car_models)
    year = st.selectbox("Select Year", years)
    fuel_type = st.selectbox("Select Fuel Type", fuel_types)
    driven = st.number_input("Enter Kilometers Driven", min_value=0, step=1000)

    if st.button("Predict Price"):
        try:
            # Encode input
            company_encoded = encoders['company_encoder'].transform([company])[0]
            name_encoded = encoders['name_encoder'].transform([car_model])[0]
            fuel_type_encoded = encoders['fuel_type_encoder'].transform([fuel_type])[0]

            # Input array
            input_data = np.array([name_encoded, company_encoded, int(year), int(driven), fuel_type_encoded]).reshape(1, 5)

            prediction = model.predict(input_data)
            st.success(f"Predicted Price: ₹ {np.round(prediction[0], 2)}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

else:
    st.warning("⚠️ Model not loaded. Please upload required files.")
