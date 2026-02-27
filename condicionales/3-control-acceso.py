import random as rd

USER = "santiago"
PASSWORD = "123"
user_in = input("Enter your username: ")
password_in = input("Enter Your Password")
if user_in == USER and password_in == PASSWORD:
    auth_code = rd.randint(100, 999)
    print("Auth code sent\nYour auth code is: ", auth_code)
    auth_code_in = int(input("Please, enter your auth code: "))
    if auth_code_in == auth_code:
        print("Welcome ", USER, " To your account")
    else:
        print("Invalid authentication code")
else:
    print("Invalid username or password")
