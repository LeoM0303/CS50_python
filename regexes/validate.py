email = input("Enter your email: ").strip()

if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")
