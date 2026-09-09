import streamlit as st
import json


st.title("Register")

# Role selection
r = st.selectbox(
    "Select Role",
    ["User", "Admin"]
)

# Registration form
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

    btn = st.form_submit_button("Register")

    if btn:
        # Check required fields
        if not n or not e or not p or not c_p:
            st.error("Please fill in all fields.")

        # Check passwords
        elif p != c_p:
            st.error("Passwords do not match.")

        else:
            # Create new user dictionary
            new_user = {
                "name": n,
                "email": e,
                "password": p,
                "c_password": c_p,
                "role": r
            }

            # Read existing users
            if os.path.exists("users.json"):
                with open("users.json", "r") as r_file:
                    try:
                        all_users = json.load(r_file)
                    except json.JSONDecodeError:
                        all_users = []
            else:
                all_users = []

            # Add new user
            all_users.append(new_user)

            # Save users
            with open("users.json", "w") as w_file:
                json.dump(all_users, w_file, indent=4)

            st.success("Successfully registered!")

            # Go to login page
            st.switch_page("pages/login.py")