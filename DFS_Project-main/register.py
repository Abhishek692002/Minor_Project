import streamlit as st
from database import add_user

def register_user():
    st.write("### Create a New Account")
    name = st.text_input("Full Name")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password != confirm_password:
            st.error("Passwords do not match")
        elif len(username.strip()) == 0 or len(password.strip()) == 0:
            st.error("Username and Password cannot be empty")
        else:
            success = add_user(username, password, name)
            if success:
                st.success("Account created successfully! Please login.")
            else:
                st.error("Username already exists. Try another one.")
