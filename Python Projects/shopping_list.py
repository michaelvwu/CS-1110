# Michael Wu (mvw5mf)

shopping_list = []

# Read the file into the list
datafile = open("shopping_list.txt", "r")

for line in datafile:
    line = line.strip()
    shopping_list.append(line)
datafile.close()

print("Your current shopping list is:")
for item in shopping_list:
    print(item)

print()
while True:
    item_to_add = input("Items to add (NONE to stop): ")
    if item_to_add.upper() == "NONE":
        break
    shopping_list.append(item_to_add)

print()
while True:
    item_to_remove = input("Items to remove (NONE to stop): ")
    if item_to_remove.upper() == "NONE":
        break
    shopping_list.remove(item_to_remove)

print()
print("Your current shopping list is:")
for item in shopping_list:
    print(item)

print()
print("Saving to shopping_list.txt...")
datafile = open("shopping_list.txt", "w")

for item in shopping_list:
    datafile.write(item + "\n")