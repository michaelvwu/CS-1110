# Michael Wu (mvw5mf) and Cesar Roucco (cr3fd)
import random

restaurants = ["Sticks", "Yuan Ho", "Melting Pot", "East Garden"]
styles = ["Casual", "Chinese", "Fancy", "Chinese"]
costs = ["$", "$", "$$$", "$$"]

def get_random_restaurant():
    pick = random.randint(0, 3)
    r = (restaurants[pick])
    s = (styles[pick])
    c = (costs[pick])
    return(r, s, c)

def get_restaurant_style(chosen_style):
    list_here = []
    list_cost = []
    for i in range(len(styles)):
        if styles[i] == chosen_style:
            list_here.append(restaurants[i])
            list_cost.append(costs[i])
        else:
            continue
    indexing = random.randint(0, len(list_here)-1)
    r = list_here[indexing]
    s = chosen_style
    c = list_cost[indexing]
    return(r,s,c)

def get_restaurant_cost(chosen_cost):
    list_here = []
    list_style = []
    for i in range(len(costs)):
        if costs[i] == chosen_cost:
            list_here.append(restaurants[i])
            list_style.append(styles[i])
        else:
            continue
    indexing = random.randint(0, len(list_here)-1)
    r = list_here[indexing]
    s = list_style[indexing]
    c = chosen_cost
    return(r,s,c)


print("Welcome to WahooSpoon!")
print("1. Get a random restaurant")
print("2. Get a random restaurant based on style")
print("3. Get a random restaurant based on cost")
choice = int(input("Choice?: "))
if choice == 1:
    r, s, c = get_random_restaurant()
elif choice == 2:
    print(set(styles))
    style = input("What style would you like?: ")
    r, s, c = get_restaurant_style(style)
else:
    print(set(costs))
    cost = input("What cost would you like?: ")
    r, s, c = get_restaurant_cost(cost)

print("We're going to", r, "today! (Style:", s, "/ Cost:", c, ")")