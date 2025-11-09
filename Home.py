import streamlit as st
from auth import login
from register import register_user
from database import init_db

# Set page config
st.set_page_config(page_title="DFS App", layout="centered")


# Initialize DB
init_db()

st.sidebar.title("Navigation")
menu = ["Login", "Sign Up"]
choice = st.sidebar.radio("Menu", menu)

if choice == "Login":
    (name, auth_status, username), _ = login()

    if auth_status:
        st.success(f"Welcome {name} 🎉")
        st.info("Go to the sidebar → DFS Checker to start your test.")

        if st.button("Logout"):
            st.session_state.clear()
            st.experimental_rerun()

    elif auth_status is False:
        st.error("❌ Username/Password incorrect")
    elif auth_status is None:
        st.warning("👤 Please enter your login details")

elif choice == "Sign Up":
    register_user()
