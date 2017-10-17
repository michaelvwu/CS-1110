# Michael Wu (mvw5mf)

scores = input("Input your scores, separated by spaces: ").split()
score_list = [int(x) for x in scores]
# print(score_list)

average = float(sum(score_list)/len(score_list))


if 93 <= float(average):
    letter = "A"
elif 90 <= float(average) < 93:
    letter = "A-"
elif 87 <= float(average) < 90:
    letter = "B+"
elif 83 <= float(average) < 87:
    letter = "B"
elif 80 <= float(average) < 83:
    letter = "B-"
elif 77 <= float(average) < 80:
    letter = "C+"
elif 73 <= float(average) < 77:
    letter = "C"
elif 70 <= float(average) < 73:
    letter = "C-"
elif 67 <= float(average) < 70:
    letter = "D+"
elif 63 <= float(average) < 67:
    letter = "D"
elif 60 <= float(average) < 63:
    letter = "D-"
else:
    letter = "F"

# if average.is_integer():
#     print("Average: " + str(int(average)))
# else:
#     print("Average: " + str(format(average, '.3f')))
print("Average: " + format(average,'.3f'))
print("Letter: " + letter)