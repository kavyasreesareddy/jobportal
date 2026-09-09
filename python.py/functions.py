# Functions with only return keywords but not with arguments and parameters

# remail = "vamsi@gmail.com"
# rpassword = "vamsi@123"


# def login():
#     lemail = input("Enter email to login: ")
#     lpassword = input("Enter password to login: ")

#     if lemail == remail and lpassword == rpassword:
#         print("Login successful")
#         return True
#     else:
#         print("Login failed")
#         return False


# op = login()

# if op == True:
#     print("Dashboard")
# else:
#     print("Try again")


#functions with variables-length arguments (*arguments)
def abc(*p):
    print(p)
abc(1,2,3)
# 2. functions with keywords arguments

def destils(names, age):
    print(names, age)
deatils(name="vamsi", age=23) 

# 3. functions with variables-length keywords aruguments

def details(**p):
    print(p)
details1(name="vamsi", age=23,)
