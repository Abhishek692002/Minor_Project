import streamlit as st
from database import get_user

def login():
    st.write("### Login to Your Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    login_btn = st.button("Login")

    if login_btn:
        user = get_user(username, password)
        if user:
            name, username = user
            # store login in session
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["name"] = name
            return (name, True, username), None
        else:
            return (None, False, None), None

    return (None, None, None), None
