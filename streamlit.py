import streamlit as st
st.title("Hai")
name=st.text_input("Enter your name")
age=st.number_input("Enter your age")
def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64("background.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{robo}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
if st.button("Submit"):
  st.write(f"Hello,{name},age is {age}")
