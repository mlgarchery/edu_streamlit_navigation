import streamlit as st
from app_one import renderApp1
from app_two import renderApp2

st.title("Session stage")
"st.session_stage", st.session_state

if "current" not in st.session_state:
    st.session_state["current"] = "app1"

def renderApps():
    if st.session_state["current"] == "app1":
        renderApp1()
    else:
        renderApp2()

def navigate():
    if st.button("Change App"):
        if st.session_state["current"] == "app1":
            st.session_state["current"] = "app2"
        elif st.session_state["current"] == "app2":
            st.session_state["current"] = "app1"

navigate()
renderApps()