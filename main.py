users = {
    "admin": "1234",
    "user": "1111"
}

def login(username, password):

    if username in users:

        if users[username] == password:
            return True

    return False


u = input("Username: ")
p = input("Password: ")

if login(u, p):
    print("Login successful")
else:
    print("Login failed")
