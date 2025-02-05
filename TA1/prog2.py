sum = 0
input_str = input("Enter digits: ")

for digit in input_str:
    if digit.isdigit():
        sum += int(digit)

print("Sum of digits:", sum)