#check users only with gmail email

email = input("Enter your email: ").strip()

username, domain = email.split("@")

if username and domain.endswith("gmail.com"):
    print("Valid username")
else:
    print("Invalid username")