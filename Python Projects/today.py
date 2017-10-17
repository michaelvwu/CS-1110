# Michael Wu (mvw5mf)

import random

# def multiply(x):
#     print(x)
#     y = x*2
#     void function no return value
#     print(y)

def multiply(x):
    # print(x)
    y = x*2
    return y
#     note this is not a void function:

def check_bigger(x,y):
    if x>y:
        return True
    else:
        return False

result = multiply(2)
print(check_bigger(8,9))
print(result)

num = random.randint(1,6)
def check(x,y):
    return x*y -1

# list are mutable, ability to change values in storage