import streamlit as st
from modules.database import add_user, get_all_users, update_status

def admin_dashboard():

    st.subheader("🛠 Admin Dashboard — Manage Users")

    st.markdown("---")
    st.markdown("### ➕ Create New User")

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password")
    if st.button("Create User"):
        try:
            add_user(new_username, new_password)
            st.success("User created successfully.")
        except:
            st.error("Username already exists.")

    st.markdown("---")
    st.markdown("### 👥 Existing Users")

    users = get_all_users()
    for user in users:
        username, role, status = user
        col1, col2, col3, col4 = st.columns([3,2,2,3])
        with col1:
            st.write(username)
        with col2:
            st.write(role)
        with col3:
            st.write(status)
        with col4:
            if status == "active":
                if st.button(f"Block {username}", key=f"block_{username}"):
                    update_status(username, "blocked")
                    st.rerun()
            else:
                if st.button(f"Unblock {username}", key=f"unblock_{username}"):
                    update_status(username, "active")
                    st.rerun()

    st.markdown("---")
