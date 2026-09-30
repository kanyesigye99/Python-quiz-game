correct_password = "marion"
other_password = "Marion10"
password= input("Enter your password: \n")
if password == correct_password or other_password:
    print("Access Granted")
else:
    print("Wrong Password")