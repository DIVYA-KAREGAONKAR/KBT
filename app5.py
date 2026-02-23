import streamlit as st

st.title("Registration Form")

# Add a 'key' to make every input unique
first_name = st.text_input("First Name", key="fname_input")
last_name = st.text_input("Last Name", key="lname_input")

gender = st.selectbox("Gender", ["Male", "Female", "Other"], key="gender_select")

email = st.text_input("Email", key="email_input")
phoneno = st.text_input("Phone Number", key="phone_input")

if st.button("Submit", key="submit_btn"):
    st.write("Done!")


st.markdown("""
<style>
    input {
        background-color: white;
        border-radius: 5px;
    }

  
    button {
        background-color: green ;
        color: white ;
        border-radius: 20px ;
    }
</style>
""", unsafe_allow_html=True)