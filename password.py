import random
import string

def random_password(l):
    numbers=string.digits
    symbols=string.punctuation
    words=string.ascii_letters
    
    total=numbers+symbols+words
    password= "".join(random.sample(total,l))
    
    return password
n=int(input())
password=random_password(n)
print(password)