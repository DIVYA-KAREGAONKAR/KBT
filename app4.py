import streamlit as st
st.title("Welcome to My Streamlit App")
age=st.slider("Select your age:", 1,100)
city=st.selectbox("Select your city:", ["Delhi", "Mumbai", "Nashik", "Pune"])

if st.button("Submit"):
    st.write(f"You are {age} years old and you live in {city}.")

st.markdown("""

    <style>
        .stSlider {
            background-color: #f0f0f0;
            border-radius: 10px;
            padding: 10px;              
        }
        .stSelectbox {
            background-color: #f0f0f0;
            border-radius: 10px;
            padding: 10px;
        }
        .stButton {
            background-color: #4CAF50;
            color: white;   
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            cursor: pointer;
        }
        .stButton:hover {
            background-color: #45a049;
        }
    </style>
            """, unsafe_allow_html=True
)