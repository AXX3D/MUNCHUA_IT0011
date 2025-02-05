row = 1
num = 1
while row <= 4:
    spaces = " " * (4 - row)
    print(spaces + str(2 * row - 1) * (2 * row - 1))
    row += 1