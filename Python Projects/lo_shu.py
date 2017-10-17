# Nancy Zhang (nz2bc)
# Michael Wu  (mvw5mf)

num = [['', '', ''], ['', '', ''], ['', '', '']]

a, b, c, d, e, f, g, h, i = input("Numbers: ").split()

row1 = [a, b, c]
row2 = [d, e, f]
row3 = [g, h, i]

num_square1 = [int(x) for x in row1]
num_square2 = [int(y) for y in row2]
num_square3 = [int(z) for z in row3]

summation_row1 = sum(num_square1)
summation_row2 = sum(num_square2)
summation_row3 = sum(num_square3)

column_01 = [a, d, g]
column_11 = [b, e, h]
column_21 = [c, f, i]

column_0 = [int(x) for x in column_01]
column_1 = [int(y) for y in column_11]
column_2 = [int(z) for z in column_21]

summation_col1 = sum(column_0)
summation_col2 = sum(column_1)
summation_col3 = sum(column_2)
summations = summation_col1, summation_col2, summation_col3, summation_row1, summation_row2, summation_row3

diagonal1 = [a, e, i]
diagonal2 = [g, e, c]

diag_0 = [int(x) for x in diagonal1]
diag_1 = [int(y) for y in diagonal2]

if sum(diag_0) == 15:
    if sum(diag_1) == 15:
        while summations != 15:
            if summation_row1 != 15:
                print(row1, "fails the test!")
            if summation_row2 != 15:
                print(row2, "fails the test!")
            if summation_row3 != 15:
                print(row3, "fails the test!")
            if summation_col1 != 15:
                print("Column 0 fails the test!")
            if summation_col2 != 15:
                print("Column 1 fails the test!")
            if summation_col3 != 15:
                print("Column 2 fails the test!")
            print("This is not a Lo Shu Magic Square")
            break
        else:
            print("This is a valid Lo Shu Magic Square!")