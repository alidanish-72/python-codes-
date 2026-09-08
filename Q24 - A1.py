# Login Validator: Check if username and password are valid
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin123":
    print("Login successful")
else:
    print("Invalid username or password")
