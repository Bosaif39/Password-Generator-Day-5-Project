import random

#lists for small letters, big  letters, symbols and numbers
alphabetSmall = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

alphabetBig =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '^', '_', '`', '{', '|', '}', '~']

#ask the user for the number of characters per type
letterSmall=int(input("How manny small letters in the password? :"))
letterBig=int(input("How manny big letters in the password? :"))
sym=int(input("How manny symbols? :"))
num=int(input("How manny numbers? :"))

#pick random characters for each type 
ranletterSmall=list(range(letterSmall))
for i in ranletterSmall:
    ranletterSmall[i]=random.choice(alphabetSmall)

ranletterBig=list(range(letterBig))
for i in ranletterBig:
    ranletterBig[i]=random.choice(alphabetBig)

rannum=list(range(num))
for i in rannum:
    rannum[i]=random.choice(numbers)
    
ransym=list(range(sym))
for i in ransym:
    ransym[i]=random.choice(symbols)

#conctenat the characters and shuffle them to make strong password
passwordd=ranletterSmall+rannum+ransym+ranletterBig
random.shuffle(passwordd)
password1="".join(passwordd)
print(password1)





