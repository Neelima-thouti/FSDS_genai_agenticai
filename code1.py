import streamlit as st
import pandas as pd
import numpy as np

st.title("My first Streamlit app")
st.write("This is simple app to demonstaret basic functionalities of streamlit")

st.sidebar.header("User input features")

user_name=st.sidebar.text_input("What is your name?","Streamlit User")
age=st.sidebar.slider("Select your age",0,100,25)

favorite_color=st.sidebar.selectbox("What is your favorite color?",["Blue","Red","Yellow","Green"])

st.header(f"Welcome,  {user_name}!")
st.write(f"You are {age} years old and favorite color is {favorite_color} .")

st.subheader("Here's some random data:")

data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye")
