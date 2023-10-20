import random
import string

def generate_password(username, length=12):
    # Combine the username with some random characters
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=length - len(username)))
    password = username + random_chars
    return password

username = input("Enter your name: ")
password = generate_password(username)
print("Your generated password is:", password)
