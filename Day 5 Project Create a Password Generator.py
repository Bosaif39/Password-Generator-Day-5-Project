import random

#lists for small letters, big  letters, symbols and numbers
alphabetSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabetBig =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '^', '_', '`', '{', '|', '}', '~']

#ask the user for the number of characters per type


#A function to make passwords
def password(passwordLen):
    if passwordLen < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    # Randomly distribute the password length among the categories
    remainingLength = passwordLen

    # Ensure at least one character of each type is present
    letterSmall = random.randint(1, remainingLength - 3)
    remainingLength -= letterSmall
    letterBig = random.randint(1, remainingLength - 2)
    remainingLength -= letterBig
    sym = random.randint(1, remainingLength - 1)
    remainingLength -= sym
    num = remainingLength

    # Pick random characters for each category
    ranletterSmall = [random.choice(alphabetSmall) for _ in range(letterSmall)]
    ranletterBig = [random.choice(alphabetBig) for _ in range(letterBig)]
    rannum = [random.choice(numbers) for _ in range(num)]
    ransym = [random.choice(symbols) for _ in range(sym)]

    # Concatenate the characters and shuffle them to create a strong password
    password_chars = ranletterSmall + ranletterBig + rannum + ransym
    random.shuffle(password_chars)
    password1 = "".join(password_chars)
    
    return password1

print("This is a 8 charcters long password:")
passw=password(8)
print(passw)
print("="*10)

test=input("Do you want another password? type y to make another on, otherwise type n: ").lower()
if(test=="y"):
    num=int(input("What is the lenght of it? type an intger greater than or equal 8: "))
    print("="*10)
    passw=password(num)
    print(len(passw))
    print(f"{passw}")


    




