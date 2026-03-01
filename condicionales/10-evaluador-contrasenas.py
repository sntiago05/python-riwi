errors_message = []
password = input("Enter your password: ")

if len(password) < 8:
    errors_message.append("Must be at least 8 characters")

if not any(c.isdigit() for c in password):
    errors_message.append("Must include at least one number")

if not any(c.isalpha() for c in password):
    errors_message.append("Must include at least one letter")

if " " in password:
    errors_message.append("Must not contain spaces")

if len(errors_message) > 0:
    print(f"Recommendations for your password:\n{'\n'.join(errors_message)}")
else:
    print("Your password is secure")