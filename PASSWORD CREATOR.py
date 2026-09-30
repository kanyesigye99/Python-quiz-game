#get the password from the user
#password = '1234'
password = input("Enter your password: ")

if len(password) >= 4:
    print("Accepted")

    name = input("Enter Username: ")

    if len(name) > 0:
        print("Name Accepted")
    else:
        print("Get another name")
else:
    print("Password is too short, choose another one")
