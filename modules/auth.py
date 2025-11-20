import streamlit as st
from modules.database import get_user

def login_screen():
    st.subheader("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user(username, password)

        if user is None:
            st.error("Invalid username or password.")
            return None

        username, role, status = user

        if status == "blocked":
            st.error("🚫 App blocked — contact administrator.")
            return None

        # Save session
        st.session_state["logged_in"] = True
        st.session_state["username"] = username
        st.session_state["role"] = role

        st.success(f"Welcome {username}!")
        st.rerun()

    return None
