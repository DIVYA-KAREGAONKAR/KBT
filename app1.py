import streamlit as st 

st.title("Basic Calculator")
num1=st.number_input("Enter your First Number:",format="%d")
num2=st.number_input("Enter your Second Number:",format="%d")
operation=st.selectbox("Choose Operation" ,["Add","Sub","Mul","Div"])

if st.button("Calculate"):
    if operation == "Add":
        st.write("Addition:" ,num1+num2)
    elif operation == "Sub":
        st.write("Subtraction:",num1-num2)
    elif operation =="Mul":
        st.write("Multiplication:",num1*num2)
    elif operation == "Div":
        if num2!=0:
            st.write("Division:",num1/num2)
        else:
            st.write("Cannot divide by Zero")