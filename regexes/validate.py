email = input("Enter your email: ").strip()

username, domain = email.split("@")

if username and "." in domain:
    print("Valid username")
else:
    print("Invalid username")