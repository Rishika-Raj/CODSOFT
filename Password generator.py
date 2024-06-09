import random
import string

def generate_password(length):
    if length < 9:
        print("Password length should be at least 9 characters.")
        return None
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired password length (at least 9 characters): "))
            if length < 9:
                print("password length should be at least 9 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    password = generate_password(length)
    if password:
        print("Generated Password: ", password)
        
if __name__ == "__main__":
    main()                