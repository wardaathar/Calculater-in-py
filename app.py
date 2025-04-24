import streamlit as st

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

st.title("Simple Calculator")

operation = st.selectbox("Operation Select karo", ["Add", "Subtract", "Multiply", "Divide"])

num1 = st.number_input("Pehla number dalo", value=0.0)
num2 = st.number_input("Dusra number dalo", value=0.0)

if st.button("Calculate karo"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"Result: {num1} / {num2} = {result}")
