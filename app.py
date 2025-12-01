import streamlit as st

st.title("🧮 Simple Calculator (Addition Only)")

# Inputs
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Button
if st.button("Calculate"):
    result = num1 + num2
    st.success(f"The result is: {result}")
