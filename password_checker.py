password = input("Enter a password to check: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(not char.isalnum() for char in password):
    score += 1

print("\nPassword Assessment:")

if score <= 2:
    print("Weak password")
elif score <= 4:
    print("Moderate password")
else:
    print("Meets the basic complexity checks")

print("Score:", score, "/ 5")
