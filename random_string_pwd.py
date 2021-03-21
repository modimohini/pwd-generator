import random
import string 

def autoPwdGenerator(length):    
    
    specialchar = string.punctuation      # to have Puncuation in PWD
    autoPwd = ''.join(random.choice(specialchar) for i in range(length)) # Choice will repeat charater to have non repeating use sample
    print(autoPwd)

autoPwdGenerator(10)                       # Specify the length of Password

# Using 'sample' for non-repeating chars in pwd
for i in range(5):
    chars = string.ascii_letters            # to have chars in PWD
    nonRepeatPwd = ''.join(random.sample(chars, 7)) 
    print(nonRepeatPwd)



