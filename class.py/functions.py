remail = "kavyasreesareddy@gmail.com"
rpassword = "kavya@123"

def login():
    lemail = input("Enter email to login: ")
    lpassword = input("Enter password to login: ")

    if remail == lemail and rpassword == lpassword:
        print("Login successfully")
        return True
    else:
        print("Invalid credentials")
        return False

op = login()

if op == True:
    print("Dashboard")
else:
    print("Login failed")
