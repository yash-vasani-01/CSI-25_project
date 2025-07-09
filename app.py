import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.set_page_config(page_title="🏡 House Price Estimator", page_icon="💰", layout="centered")

st.markdown("""
    <style>
    .main {
        background: linear-gradient(to right, #f0f2f6, #ffffff);
        padding: 2rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    .title {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #34495e;
        text-align: center;
        margin-bottom: 1rem;
    }
    .stButton>button {
        background-color: #2980b9;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        transition: background 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1abc9c;
    }
    </style>
""", unsafe_allow_html=True)

model = joblib.load("model.pkl")
columns = joblib.load("columns.pkl")
zip_columns = [col for col in columns if col.replace('.', '', 1).isdigit()]

# st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🏠 Smart House Price Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Estimate property value based on key features</div>', unsafe_allow_html=True)

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        bedrooms = st.slider("🛏 Bedrooms", 1, 10, 3)
        bathrooms = st.slider("🛁 Bathrooms", 1, 5, 2)
        condition = st.slider("🏚 Condition (1 = Poor, 5 = Excellent)", 1, 5, 3)
        yr_built = st.slider("🏗 Year Built", 1900, 2024, 2005)
        age_of_property = 2024 - yr_built

    with col2:
        floors = st.selectbox("🏢 Floors", [1.0, 1.5, 2.0, 2.5, 3.0])
        sqft_living = st.number_input("📏 Sqft Living Area", 500, 10000, 2000)
        sqft_living15 = st.number_input("📐 Sqft Living15 (Neighborhood)", 500, 10000, 1800)
        price_per_sqft = st.number_input("💵 Price per Sqft", 50.0, 2000.0, 300.0)
        zipcode = st.selectbox("📍 Zipcode", zip_columns)

    submit = st.form_submit_button("🔍 Predict Price")

if submit:
    base_data = {
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft_living": sqft_living,
        "sqft_living15": sqft_living15,
        "floors": floors,
        "condition": condition,
        "yr_built": yr_built,
        "age_of_property": age_of_property,
        "price_per_sqft": price_per_sqft
    }

    one_hot_zip = {col: 0 for col in zip_columns}
    one_hot_zip[zipcode] = 1

    full_input = {**base_data, **one_hot_zip}
    for col in columns:
        if col not in full_input:
            full_input[col] = 0

    input_df = pd.DataFrame([full_input])[columns]
    prediction = model.predict(input_df)[0]

    st.success(f"💰 Estimated House Price: **${prediction:,.2f}**")

st.markdown('</div>', unsafe_allow_html=True)
