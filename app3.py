import streamlit as st
st.title("Simple chatbot")
question=st.text_input("Ask me anything:")
if st.button("Submit"):
    if question:
        st.write(f"You asked: {question}")
        st.write("Chatbot is in the process of answering your question...")
    else:
        st.write("Please enter a question before submitting.")