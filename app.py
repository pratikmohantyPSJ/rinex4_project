import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('bmi')

#user input 
st.title("BMI PREDICTOR")
ip = st.text_input("Enter height:")
ip = st.text_input("Enter weight:")

#predict the bmi
op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])  
