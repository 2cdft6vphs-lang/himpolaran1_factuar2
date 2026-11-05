print("===================================")
print("      REGISTRATION FORM")
print("===================================")

while True:
    name = input("Enter your full name: ")
    if name.strip() == "":
        print("Error: Name cannot be empty!")
    elif not all(c.isalpha() or c.isspace() for c in name):
        print("Error: Name must contain letters only!")
    else:
        break
while True:
    age = input("Enter your age: ")
    if not age.isdigit():
        print("Error: Age must be a number!")
    elif int(age) < 1 or int(age) > 120:
        print("Error: Age must be between 1 and 120!")
    else:
        age = int(age)
        break

while True:
    email = input("Enter your email: ")
    if "@" in email and "." in email.split("@")[-1] and " " not in email:
        break
    else:
        print("Error: Please enter a valid email!")

while True:
    phone = input("Enter your phone number: ")
    if phone.isdigit() and len(phone) in (10, 11):
        break
    else:
        print("Error: Phone number must have 10 or 11 digits!")

while True:
    username = input("Create a username: ")
    if len(username) >= 4 and " " not in username:
        break
    else:
        print("Error: Username must have at least 4 characters and no spaces!")

while True:
    password = input("Create a password: ")
    if len(password) >= 8:
        confirm = input("Confirm your password: ")
        if password == confirm:
            break
        else:
            print("Error: Passwords do not match!")
    else:
        print("Error: Password must have at least 8 characters!")

print("\\n===================================")
print("     REGISTRATION SUCCESSFUL!")
print("===================================")
print("Full Name:", name)
print("Age:", age)
print("Email:", email)
print("Phone Number:", phone)
print("Username:", username)
print("Password: [Hidden]")
print("===================================")
print("Thank you for registering!") 