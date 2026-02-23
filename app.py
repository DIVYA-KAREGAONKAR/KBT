import streamlit as st
st.title("Hello World")
st.write("This is my first Streamlit app!")
name= st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")