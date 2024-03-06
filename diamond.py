import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

with open("diamond_model.pkl", 'rb') as f:
    model = pickle.load(f)
    print(model)

def predict_price(carat, depth, x, y, z):
  data = [[carat, depth, x, y, z]]  # Prepare data as a 2D array
  prediction = model.predict(data)[0]  # Make prediction and get the first element
  return prediction

# Streamlit app definition
st.title("Diamond Price Predictor")
st.write("Enter the diamond properties to estimate its price:")

# User input fields for diamond properties
depth = st.number_input("Depth", min_value=0.0, max_value=100.0, key="depth")
carat = st.number_input("Carat", min_value=0.0, max_value=100.0, key="carat")
x = st.number_input("X", min_value=0.0, key="x")
y = st.number_input("Y", min_value=0.0, key="y")
z = st.number_input("Z", min_value=0.0, key="z")

# Button to trigger prediction
predict_button = st.button("Predict Price")

if predict_button:
  # Make prediction if button is clicked
  predicted_price = predict_price(carat, depth, x, y, z)
  st.write(f"Predicted Price: ${predicted_price:.2f}")

