import random
import string 

chars = string.ascii_letters + string.printable + string.punctuation + string.digits

pwd = ''.join(random.choice(chars) for i in range(15))
print(pwd)

