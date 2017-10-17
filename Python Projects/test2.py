# Michael Wu (mvw5mf)

def math_thing(x):
    x = x+3
    return x

y =2

print(y)
print(math_thing(y))
print(y)

# passby value

def modify(my_list):
    my_list.append(7)
    return my_list

this_list = [2,3]
print(this_list)
print(modify(this_list))
print(this_list)
# pass by reference