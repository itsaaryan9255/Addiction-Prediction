import streamlit as st
import pickle
import numpy as np

# MUST be first Streamlit command
st.set_page_config(page_title="Addiction_Prediction", page_icon=":shark:", layout="wide")

st.title("Hello, Streamlit")

def load_model():
    return pickle.load(open("linear_regression_model .pkl", "rb"))

model = load_model()

value1 = st.number_input("Hours spent on social media")

value2 = st.selectbox("Affects Academic Performance", [0, 1])
st.write("You selected:", value2)

value3 = st.number_input("Sleep Hours Per Night")

value4 = st.selectbox("Mental Health Score", [0,1,2,3,4,5,6,7,8,9,10])
st.write("You selected:", value4)

value5 = st.selectbox("Conflicts Over Social Media", [0,1,2,3,4,5])
st.write("you selected: ",value5)


if st.button("predict"):
    input_data = np.array([[value1, value2, value3, value4, value5]])
    prediction = model.predict(input_data)
    st.write(f"Predicted Addiction Level: {prediction[0]:.2f}")