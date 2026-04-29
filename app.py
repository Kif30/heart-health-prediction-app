import pickle
import numpy as np
import streamlit as st
import pandas as pd

model = pickle.load(open('heart_model.pkl', 'rb'))

st.title('Heart Disease Prediction')

age = st.number_input('Age', min_value=1, max_value=120, value=25)
RestingBP = st.number_input('Resting Blood Pressure', min_value=0, max_value=300, value=120)
Cholesterol = st.number_input('Cholesterol', min_value=0, max_value=1000, value=200)
FastingBS = st.selectbox('Fasting Blood Sugar', (0, 1))
MaxHR = st.number_input('Max Heart Rate', min_value=0, max_value=300, value=150)
Oldpeak = st.number_input('Oldpeak', min_value=0.0, max_value=10.0, value=1.0)

Exercise_Angina = st.selectbox('Exercise Angina', ('Yes','No'))
sex = st.selectbox('Sex', ('male','female'))
Chest_PainType = st.selectbox('Chest Pain Type', ('TA','ATA','NAP','ASY'))
Resting_ECG = st.selectbox('Resting ECG', ('Normal','ST','LVH'))
st_Slope = st.selectbox('ST Slope', ('Up','Flat','Down'))

# Encoding
Exercise_Angina = 1 if Exercise_Angina == 'Yes' else 0
Sex_F = 1 if sex == 'female' else 0
Sex_M = 1 if sex == 'male' else 0

cp_map = {'TA':0,'ATA':1,'NAP':2,'ASY':3}
Chest_PainType = cp_map[Chest_PainType]

ecg_map = {'Normal':0,'LVH':1,'ST':2}
Resting_ECG = ecg_map[Resting_ECG]

slope_map = {'Up':1,'Flat':2,'Down':0}
st_Slope = slope_map[st_Slope]

# DataFrame (FIXED COLUMN NAME)
input_features = pd.DataFrame({
    'Age':[age],
    'RestingBP':[RestingBP],
    'Cholesterol':[Cholesterol],
    'FastingBS':[FastingBS],
    'MaxHR':[MaxHR],
    'Oldpeak':[Oldpeak],
    'Exercise_Angina':[Exercise_Angina],
    'Sex_F':[Sex_F],
    'Sex_M':[Sex_M],
    'Chest_PainType':[Chest_PainType],
    'Resting_ECG':[Resting_ECG],
    'st_Slope':[st_Slope]   # ✅ FIXED (was ST_Slope)
})

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_features)
    
    if prediction[0] == 1:
        st.success('The person is likely to have heart disease.')
    else:
        st.success('The person is unlikely to have heart disease.')