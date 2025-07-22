import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short!"

    # Define character sets
    letters = string.ascii_letters  # a-z and A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # special characters

    # Combine all characters
    all_chars = letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Ask user for password length
length = int(input("Enter password length: "))
password = generate_password(length)
print("Generated Password:", password)