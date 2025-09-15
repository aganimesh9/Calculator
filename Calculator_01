import streamlit as st

st.title("🧮 Web Calculator")

# Input field for expression
expression = st.text_input("Enter expression (use +, -, *, /, (), etc.):")

# Calculate when button pressed
if st.button("Calculate"):
    try:
        result = eval(expression)  # respects BODMAS
        st.success(f"Result: {result}")
    except Exception as e:
        st.error(f"Error: {e}")
