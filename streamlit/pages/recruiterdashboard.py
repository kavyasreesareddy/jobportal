import streamlit as st

st.title("Recruiter Dashboard")

# Check whether a user is logged in
if "logged_user" not in st.session_state:
    st.warning("No logged-in user is able to access this page.")
    st.switch_page("pages/login.py")

else:
    # Check whether the logged-in user is a recruiter
    if st.session_state["logged_user"]["role"] == "recruiter":
        st.success("Welcome, Recruiter!")

    else:
        st.warning("You are not a recruiter, so you cannot access this page.")
