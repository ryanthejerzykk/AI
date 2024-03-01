import hashlib
import os

# Get password from user input
password = input("Enter your password: ")

# Generate a salt
salt = os.urandom(16)

# Hash the password with the salt
hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

# Print the hashed password
print("Hashed password:", hashed_password.hex())