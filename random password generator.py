import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        return None

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password has at least one of each character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random characters from all pools
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the result to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            password = generate_password(length)
            if password:
                print(f"Generated password: {password}")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
