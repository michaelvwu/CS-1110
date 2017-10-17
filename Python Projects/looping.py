# Michael Wu (mvw5mf)

# n = 0
# while True:
#     print(n)
#     n += 1
#     if n > 10:
#         break

# refers to an index number (times of looping)
# for i in range(4):
#     break

# for grade in grade_list:
#     print("Grade: " + str(grade))
# for i in range(len(grade_list)):
#     print("Grade: " + str(grade))

# ^same things

# leaving loop, value of index restarts = scope
# for i in range(5):
#     for j in range(5):
#         print(i,j)

# number = int(input("Number: "))
# roman = " "
# i = 0
# while i < number:
#     roman += "I"
#     i += 1
# print(roman)

sum = 0
count = 0
done = False
while not done:
    price = float(input("Item Price: "))
    if price < 0:
        done = True
    else:
        sum += price
        count += 1

average = format(sum/count, '.2f')
print(average)


# total = sum(float(price))
#
# average = sum(price)/len(price)
#
# print("Total: " + str(total))
# print("Average: " + str(average))