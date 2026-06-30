import random
import string

# Password Generator Function
def generate_password(length, upper, lower, digits, symbols):
    characters = ""

    if upper:
        characters += string.ascii_uppercase
    if lower:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def password_strength(length):
    if length < 8:
        return "Weak"
    elif length < 12:
        return "Medium"
    else:
        return "Strong"


print("=" * 45)
print("        ADVANCED PASSWORD GENERATOR")
print("=" * 45)

while True:

    try:
        length = int(input("\nEnter password length: "))

        upper = input("Include Uppercase Letters? (y/n): ").lower() == "y"
        lower = input("Include Lowercase Letters? (y/n): ").lower() == "y"
        digits = input("Include Numbers? (y/n): ").lower() == "y"
        symbols = input("Include Special Characters? (y/n): ").lower() == "y"

        count = int(input("How many passwords to generate? "))

        print("\nGenerated Passwords")
        print("-" * 30)

        for i in range(count):
            password = generate_password(length, upper, lower, digits, symbols)

            if password is None:
                print("Select at least one character type.")
                break

            print(f"{i+1}. {password}")

            with open("passwords.txt", "a") as file:
                file.write(password + "\n")

        print("\nPassword Strength:", password_strength(length))
        print("Passwords saved to passwords.txt")

    except ValueError:
        print("Invalid input!")

    again = input("\nGenerate more passwords? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using Password Generator!")
        break