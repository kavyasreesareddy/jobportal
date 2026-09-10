from fastapi import FastAPI
import json

obj = FastAPI()


@obj.get("/")
def get_data():
    return {"message": "API is working"}


@obj.post("/post_data")
def post_data():
    new_user = {
        "name": "kavya",
        "email": "kavya@gmail.com",
        "role": "recruiter"
    }

    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    all_users.append(new_user)

    with open("users.json", "w") as w_file:
        json.dump(all_users, w_file)

    return {"message": "User added successfully"}


@obj.delete("/delete_user/{email}")
def delete_user(email: str):
    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:
        if user["email"] == email:
            all_users.remove(user)

            with open("users.json", "w") as w_file:
                json.dump(all_users, w_file)

            return "Successfully deleted and data updated after deletion"

    return "No valid user found"


@obj.put("/edit_user/{email}")
def edit_user(email: str, name: str, password: str):
    with open("users.json", "r") as r_file:
        all_users = json.load(r_file)

    for user in all_users:
        if user["email"] == email:
            user["name"] = name
            user["password"] = password

            with open("users.json", "w") as w_file:
                json.dump(all_users, w_file)

            return "User updated successfully"

    return "No user found with provided email"
