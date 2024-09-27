# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 05:05:34 2024

@author: bahar
"""

import streamlit as st

st.title("House Price Prediction Experiment")

# Participants adjust sliders
st.write("Please adjust the input features below and observe how the AI's house price prediction changes in response to your adjustments.")

bedrooms = st.slider('Number of Bedrooms', 1, 10, 3)
full_baths = st.slider('Number of Full Baths', 1, 5, 2)
half_baths = st.slider('Number of Half Baths', 0, 2, 1)
heating_rating = st.slider('Heating Rating', 0, 10, 5)
material_rating = st.slider('Material Rating', 0, 10, 7)
black_population_percentage = st.slider('Percentage of Black Residents', 0, 100, 50)

# AI Prediction based on input features (dynamic update)
ai_predicted_price = (bedrooms * 50000) + (full_baths * 25000) + (half_baths * 10000) + \
                     (heating_rating * 2000) + (material_rating * 3000) - (black_population_percentage * 500)

# Highlight AI Prediction
st.markdown(f"<h3 style='color:blue;'>AI's Predicted House Price: ${ai_predicted_price:.2f}</h3>", unsafe_allow_html=True)

# Display final inputs for confirmation
st.subheader("Your Input Values:")
st.write(f"Number of Bedrooms: {bedrooms}")
st.write(f"Number of Full Baths: {full_baths}")
st.write(f"Number of Half Baths: {half_baths}")
st.write(f"Heating Rating: {heating_rating}")
st.write(f"Material Rating: {material_rating}")
st.write(f"Percentage of Black Residents: {black_population_percentage}%")

# Allow participant to enter their final estimation
final_user_prediction = st.number_input('Please enter your final estimate of the house price after reviewing the AI prediction:', min_value=0, step=1000)

# Button to submit prediction
if st.button('Submit Final Estimation'):
    st.write(f"Your final house price estimation is: ${final_user_prediction:.2f}")
    # Further processing or storing of the final prediction