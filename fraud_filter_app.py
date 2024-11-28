import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

page = st.sidebar.selectbox("Explore Data or use Predictor Tool", ("Predictor", "Explore"))

if page == "Predictor":
    show_predict_page()
else:
    show_explore_page()

