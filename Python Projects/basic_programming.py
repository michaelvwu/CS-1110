# Michael Wu (mvw5mf)

# print("Python is awesome")
# print(4)

# var = 9
# print(var)
#
# print(5+9)
# value=8
# print(5+value)
# value = 8.9464686
# print(5+value)
# print(type(value))

print(9.5/2.3)
value4 = 9.5/2.3
print(type(value4))
print(type(value4) is float)

test1=4
print(test1 ==4)
print(test1 ==5)
print(type(test1 ==4))

print(format(value4, ".2f"))
print(format(value4, ".7f"))
print(format(value4, ".8f"))

print(1/3)
print(1//3)
print(float(1/3))

a = "Mark"
b = "".join(['Ma','rk'])
# content equivalence
print(a == b)
# name equivalence
print(a is b)


bob = 4
carl = 9
sally = 4
mary =8

print(bob == sally or carl == mary)
print(bob == sally and carl == mary)
print(bob * mary > 40)
print(bob * carl >= 36)

# >,<, >=, <=, and, or, not

number = int(input("Give me a number between 0 and 100 (inclusive)"))
if number < 0 or number > 100:
    print ("Learn to count...")
