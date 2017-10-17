# Michael Wu (mvw5mf)

temp = int(input("What is the temp? "))
day = str(input("what day is it? "))
# flag variable, typical boolean, that represents some type of truth

is_cold = temp <= 30

# if is_cold:
#     print("wear hat")
#     print("wear gloves")
#     print("wear coat")

if is_cold:
    print("wear coat")
else:
    print("wear shorts")

is_sunday = day = True

if is_cold:
    if is_sunday:
        print("wear nice coat")
    else:
        print ("wear shitty coat")


key = 1
if key == 1:
    print("wear hat")
elif key == 2:
    print("wear hat")
elif key == 3:
    print("wear hat")
else:
    print("wear hat")