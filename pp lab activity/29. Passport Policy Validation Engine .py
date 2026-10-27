
def validate_password(password):
    errors = []

    # 1. Minimum length
    if len(password) < 8:
        errors.append("Password must contain at least 8 characters.")

    # 2. Character categories
    if not any(c.isupper() for c in password):
        errors.append("Add at least one uppercase letter (A-Z).")

    if not any(c.islower() for c in password):
        errors.append("Add at least one lowercase letter (a-z).")

    if not any(c.isdigit() for c in password):
        errors.append("Add at least one number (0-9).")

    if not any(not c.isalnum() for c in password):
        errors.append("Add at least one special character.")

    # 3. Repeated characters
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            errors.append(
                "Do not repeat the same character 3 times consecutively."
            )
            break

    # 4. Prohibited substrings
    prohibited = ["password", "admin", "123456"]
    lower_password = password.lower()

    for word in prohibited:
        if word in lower_password:
            errors.append(
                f"Password must not contain the prohibited substring '{word}'."
            )

    # 5. Display results
    if errors:
        print("Password: INVALID")
        for error in errors:
            print("-", error)
    else:
        print("Password: VALID")
        print("All password policy rules are satisfied.")


# Test sample passwords
samples = [
    "Ab@12345",
    "hello",
    "Abc111@x",
    "Admin@1234",
    "Good#Pass9"
]

for password in samples:
    print("\nChecking:", password)
    validate_password(password)
