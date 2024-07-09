import random
import string

def generate_password(length):
    # Define the character sets to be used
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation 

    # Combine all the characters
    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Use random.choices() to generate a password with the specified length
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

def main():
    # Get desired password length from user input
    while True:
        try:
            length = int(input("Enter the desired lenth of the password: "))
            if length <= 0:
                print("Length of the password must be a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password of length {length}: {password}")

if __name__ == "__main__":
    main()
