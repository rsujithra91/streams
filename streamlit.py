import streamlit as st
st.title("Hai")
name=st.text_input("Enter your name")
age=st.number_input("Enter your age")
if st.button("Submit"):
  st.write(f"Hello,{name},age is {age}")
