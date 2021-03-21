
# to have random password generator 
import random
from numpy import random
Randomstring =["this","isso","hime", "ome"]

# Version 1
def randPwdGenerator():
    i=10
    for x in Randomstring:        
        pwdlen = random.choice(Randomstring)
        print(pwdlen)
        x=+1
randPwdGenerator()

# Version 2: with numpy
num = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','!','@','#','$','%','^','&','*','(',')']
pwd = random.choice((num), size=(10))
print(pwd)

# Version 3: with for loop 
import numpy as np
password = []
num2 = np.array([1,2,3,4,5,6,7,8,9,0])
random.shuffle(num2)
print(num2)

