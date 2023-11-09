import streamlit as st
import pandas as pd

st.title("Numeric Data Analysis Web App")
uploaded_file = st.file_uploader("Upload a numeric dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Dataset loaded successfully!")