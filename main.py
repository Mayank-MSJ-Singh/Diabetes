import pickle
import streamlit as st

#Loading Model Here
model = pickle.load(open('DMod.pkl', 'rb'))

#Making Streamlit Widgets
name = st.text_area(label="Your Name")
p = st.text_area(label="Pregnancies")
g = st.text_area(label="Glucose")
bp = st.text_area(label="BloodPressure")
stn = st.text_area(label="SkinThickness")
i = st.text_area(label="Insulin")
bmi = st.text_area(label="BMI")
dpf = st.text_area(label="DiabetesPedigreeFunction")
a = st.text_area(label="Age")

try:
    if st.button("Check"):
        y_pred = model.predict([[float(p), float(g), float(bp), float(stn), float(i), float(bmi), float(dpf), float(a)]])
        st.markdown("### Results")
        if y_pred == 1:
                st.write("Sorry to Inform You But You Have Problem, You should consult to a Doctor As Soon As Possible")
        else:
                st.write("Bingo! You are Perfectly Fine. No need to worry!")

except:
    st.write("### First Enter Details")