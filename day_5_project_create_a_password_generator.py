import random

# Character sets
lowercase_letters = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digits = list('0123456789')
special_characters = list('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

def generate_password(password_length):
    """
    Generates a random password of the specified length.

    Parameters:
    password_length (int): The length of the password to generate. Must be at least 8.

    Returns:
    str: A randomly generated password containing at least one lowercase letter, 
         one uppercase letter, one digit, and one special character.
    """
    if password_length < 8:
        raise ValueError("Password length must be at least 8 to include all character types.")

    remaining_length = password_length

    # Ensure at least one character from each category
    num_lowercase = random.randint(1, remaining_length - 3)
    remaining_length -= num_lowercase

    num_uppercase = random.randint(1, remaining_length - 2)
    remaining_length -= num_uppercase

    num_special = random.randint(1, remaining_length - 1)
    remaining_length -= num_special

    num_digits = remaining_length

    # Generate random characters for each category
    lowercase_selection = [random.choice(lowercase_letters) for _ in range(num_lowercase)]
    uppercase_selection = [random.choice(uppercase_letters) for _ in range(num_uppercase)]
    special_selection = [random.choice(special_characters) for _ in range(num_special)]
    digit_selection = [random.choice(digits) for _ in range(num_digits)]

    # Combine and shuffle the characters
    password_characters = lowercase_selection + uppercase_selection + special_selection + digit_selection
    random.shuffle(password_characters)

    # Return final password
    return ''.join(password_characters)

# Sample usage
print("This is an 8-character long password:")
generated_password = generate_password(8)
print(generated_password)
print("=" * 10)

# Ask user if they want another password
user_input = input("Do you want another password?\nType 'y' to make another one, otherwise type anything else: ").lower()

if user_input == "y":
    desired_length = int(input("What is the length of it? Type an integer greater than or equal to 8: "))
    print("=" * 10)
    new_password = generate_password(desired_length)
    print(len(new_password))
    print(new_password)
