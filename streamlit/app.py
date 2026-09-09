import streamlit as st
import json

st.title("Job Portal")

# Create two tabs
t1, t2 = st.tabs(["Login", "Register"])

# ---------------- LOGIN ----------------
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
        st.info("Login functionality coming soon...")


# ---------------- REGISTER ----------------
with t2:
    with st.form("registerform"):
        n = st.text_input(
            "Name",
            placeholder="Enter name here"
        )

        e = st.text_input(
            "Email",
            placeholder="Enter email here"
        )

        p = st.text_input(
            "Password",
            placeholder="Enter password here",
            type="password"
        )

        c_p = st.text_input(
            "Confirm Password",
            placeholder="Enter confirm password here",
            type="password"
        )

        r = st.selectbox(
            "Role",
            ["Job Seeker", "Employer"]
        )

        btn = st.form_submit_button("Register")

        if btn:
            if p != c_p:
                st.error("Passwords do not match")

            else:
                new_user = {
                    "name": n,
                    "email": e,
                    "password": p,
                    "c_password": c_p,
                    "role": r
                }

                try:
                    with open("users.json", "r") as r_file:
                        all_users = json.load(r_file)
                except FileNotFoundError:
                    all_users = []

                all_users.append(new_user)

                with open("users.json", "w") as w_file:
                    json.dump(all_users, w_file, indent=4)

                st.success("Successfully registered!")