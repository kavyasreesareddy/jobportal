import streamlit as st
import json

t1, t2 = st.tabs(["Login", "Register"])

with t1:

    with st.form("loginform"):

        e = st.text_input(
            "Enter email",
            placeholder="Enter email here"
        )

        p = st.text_input(
            "Enter password",
            placeholder="Enter password here",
            type="password"
        )

        btn = st.form_submit_button("Login")

        if btn:

            with open("users.json", "r") as r_file:
                all_users = json.load(r_file)

            user_found = False

            for user in all_users:

                if user["email"] == e and user["password"] == p:

                    user_found = True

                    # Store logged-in user
                    st.session_state["logged_user"] = {
                        "email": e,
                        "password": p,
                        "role": user["role"]
                    }

                    # Recruiter
                    if user["role"] == "recruiter":

                        st.success(
                            "Logged in as recruiter successfully. "
                            "Navigating to recruiter dashboard..."
                        )

                        st.switch_page("pages/recruiter_dashboard.py")

                    # Jobseeker
                    elif user["role"] == "jobseeker":

                        st.success(
                            "Logged in as jobseeker successfully. "
                            "Navigating to jobseeker dashboard..."
                        )

                        st.switch_page("pages/jobseeker_dashboard.py")

                    break

            if not user_found:
                st.error("User not found with those credentials.")

