# to generate random pwd with fix count of letter, digits, symbols
import string 
import random

def complexPwd():

    allTypeChar = string.digits + string.punctuation + string.ascii_letters

    pwd = random.choice(string.ascii_lowercase)     # pwd must have lowercase
    pwd += random.choice(string.ascii_uppercase)    # pwd must have uppercase
    pwd += random.choice(string.punctuation)        # pwd must have puncuation
    pwd += random.choice(string.digits)             # pwd must have digit
    print(pwd)

    for i in range(3):
        pwd += random.choice(allTypeChar)

    pwd_list = list(pwd)
    random.SystemRandom().shuffle(pwd_list)
    pwd = ''.join(pwd_list)
    return pwd

print(complexPwd())
