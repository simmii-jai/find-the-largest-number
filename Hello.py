import streamlit as st
from streamlit.logger import get_logger

import streamlit as st

st.title('FIND LARGEST AMONG GIVEN 3 NUMBERS')

st.header('Inputs: ')

number1 = st.number_input('Enter the First number')
number2 = st.number_input('Enter the second number')
number3 = st.number_input('Enter the Third number')

def maximum():
  lis = [number1 , number2 , number3]
  a = max(lis)
  st.success(f"The Largest number is {a}")

if st.button("Find the Answer"):
    maximum()
