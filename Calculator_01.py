import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")

# Store expression in session state so it persists
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Display the current expression
st.text_input("Expression", st.session_state.expression, key="display", disabled=True)

# Function to update expression
def press(key):
    st.session_state.expression += str(key)

# Function to clear
def clear():
    st.session_state.expression = ""

# Function to evaluate
def calculate():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except:
        st.session_state.expression = "Error"

# Layout buttons like a phone calculator
cols = [st.columns(4) for _ in range(5)]

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", "(", ")", "+"],
    ["C", "=", "."]
]

for row, row_vals in enumerate(buttons):
    for col, val in enumerate(row_vals):
        if val == "C":
            cols[row][col].button("C", on_click=clear)
        elif val == "=":
            cols[row][col].button("=", on_click=calculate)
        else:
            cols[row][col].button(val, on_click=press, args=(val,))
