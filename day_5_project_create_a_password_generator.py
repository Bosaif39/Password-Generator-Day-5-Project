import random

alphabetSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetBig = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '^', '_', '`', '{', '|', '}', '~']

def password(passwordLen):
    """
    Generates a random password of the specified length.

    Parameters:
    passwordLen (int): The length of the password to generate. Must be at least 4.

    Returns:
    str: A randomly generated password containing at least one lowercase letter, 
         one uppercase letter, one number, and one symbol.

    Raises:
    ValueError: If passwordLen is less than 8.

    How it works:
    1-Get the total length of the password that the user wants.

    2-Pick a random number of lowercase letters, but leave enough room to include at least one of each of the other types (uppercase letters, symbols, numbers).

    3-Substrace the number of lowercase letters from the total length.

    4-Do step 2 & 3 for uppercase letters.

    5-Do step 2 & 3 for symbols.

    6-The remaining length is the number of symbols in the password
    
    """
    if passwordLen < 8:
        raise ValueError("Password length must be at least 4 to include all character types.")

    remainingLength = passwordLen

    #Ensure at least one character from each category
    letterSmall = random.randint(1, remainingLength - 3)
    remainingLength -= letterSmall
    letterBig = random.randint(1, remainingLength - 2)
    remainingLength -= letterBig
    sym = random.randint(1, remainingLength - 1)
    remainingLength -= sym
    num = remainingLength

    #Generate random characters for each category
    ranletterSmall = [random.choice(alphabetSmall) for i in range(letterSmall)]
    ranletterBig = [random.choice(alphabetBig) for i in range(letterBig)]
    rannum = [random.choice(numbers) for i in range(num)]
    ransym = [random.choice(symbols) for i in range(sym)]

    #Combine and shuffle the characters to create the final password
    password_chars = ranletterSmall + ranletterBig + rannum + ransym
    random.shuffle(password_chars)
    password1 = "".join(password_chars)
    
    return password1

print("This is an 8-character long password:")
passw = password(8)
print(passw)
print("="*10)

test = input("Do you want another password?\nType 'y' to make another one, otherwise type anything else: ").lower()
if (test == "y"):
    num = int(input("What is the length of it? Type an integer greater than or equal to 8: "))
    print("="*10)
    passw = password(num)
    print(len(passw))
    print(f"{passw}")
