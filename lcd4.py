import streamlit as st
import json
import requests
import os
import pickle
import joblib
import numpy as np
url = 'https://github.com/adityapande403/smlproject/blob/58662b0b10d9891d708968f6cb1de8e7605263f3/Trained_model.sav'
filename = 'Trained_model.sav'
 

def normalize_option(option):
 return option.lower() in ['yes', 'true', '1', 'y']
def predict(data):
 loaded_model = joblib.load('/Users/User/Downloads/Trained_model.sav')
 prediction = loaded_model.predict(data.reshape(1, -1))
 return prediction[0]

st.title("Lung Cancer Risk Assessment")

gender = st.radio("Select your gender:", ["Male", "Female"])
age = st.number_input("Enter your age:", value=18, min_value=0, max_value=150)

smoking = normalize_option(st.radio("Do you smoke?", ["Yes", "No"]))
yellow_fingers = normalize_option(st.radio("Do you have yellow fingers?", ["Yes", "No"]))
anxiety = normalize_option(st.radio("Do you suffer from anxiety?", ["Yes", "No"]))
peer_pressure = normalize_option(st.radio("Do you feel peer pressure to smoke?", ["Yes", "No"]))
chronic_disease = normalize_option(st.radio("Do you have any chronic disease?", ["Yes", "No"]))
fatigue = normalize_option(st.radio("Do you experience fatigue?", ["Yes", "No"]))
allergy = normalize_option(st.radio("Do you have any allergies?", ["Yes", "No"]))
wheezing = normalize_option(st.radio("Do you experience wheezing?", ["Yes", "No"]))
alcohol_consuming = normalize_option(st.radio("Do you consume alcohol?", ["Yes", "No"]))
coughing = normalize_option(st.radio("Do you experience coughing?", ["Yes", "No"]))
shortness_of_breath = normalize_option(st.radio("Do you experience shortness of breath?", ["Yes", "No"]))
swallowing_difficulty = normalize_option(st.radio("Do you have difficulty swallowing?", ["Yes", "No"]))
chest_pain = normalize_option(st.radio("Do you experience chest pain?", ["Yes", "No"]))

inputs = {
"GENDER": gender,
"AGE": age,
"SMOKING": smoking,
"YELLOW_FINGERS": yellow_fingers,
"ANXIETY": anxiety,
"PEER_PRESSURE": peer_pressure,
"CHRONIC DISEASE": chronic_disease,
"FATIGUE": fatigue,
"ALLERGY": allergy,
"WHEEZING": wheezing,
"ALCOHOL CONSUMING": alcohol_consuming,
"COUGHING": coughing,
"SHORTNESS OF BREATH": shortness_of_breath,
"SWALLOWING DIFFICULTY": swallowing_difficulty,
"CHEST PAIN": chest_pain,
"LUNG_CANCER": ""
}

if st.button("Predict Health Diagnosis"):
 inputs_array = np.array(list(inputs.values())[1:], dtype=bool)
 prediction = predict(inputs_array)
   return 0
if prediction == 0:
  st.write("You have a low risk of developing lung cancer")
else:
  st.write("You have a high risk of developing lung cancer")
st.write("Inputs:")
st.write(inputs)
