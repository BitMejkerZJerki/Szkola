import random

def losuj():
    return random.randint(0,100), random.randint(0,100), random.randint(0,100)

print(losuj())


def delta():
    a,b,c = losuj()

    print(b*b-4*(a*c))

print(delta())
    
