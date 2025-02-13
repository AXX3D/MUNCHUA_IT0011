def is_palindrome(num):
    return str(num) == str(num)[::-1]

with open("TECHNICALMIDTERM/numbers.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        total_sum = sum(map(int, line.strip().split(',')))
        status = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
        print(f"Line {line_number}: {line.strip()} (sum {total_sum}) - {status}")
