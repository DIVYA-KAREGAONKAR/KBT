import streamlit as st
st.title("Welcome to My Streamlit App")
age=st.slider("Select your age:", 1,100)
city=st.selectbox("Select your city:", ["Delhi", "Mumbai", "Nashik", "Pune"])

if st.button("Submit"):
    st.write(f"You are {age} years old and you live in {city}.")