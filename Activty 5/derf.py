def divide(a, b):
    if b == 0:
        print("Denominator must not be zero")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Denominator must not be zero")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Second number must be greater or equal to the first number")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\nMENU:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        choice = input("Pick your calculator: ").strip().upper()

        if choice == 'Q':
            print("Bye Bye")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Please enter valid numbers")
                continue
            
            if choice == 'D':
                result = divide(num1, num2)
            elif choice == 'E':
                result = exponentiation(num1, num2)
            elif choice == 'R':
                result = remainder(num1, num2)
            elif choice == 'F':
                result = summation(num1, num2)
            
            if result is not None:
                print("Result:", result)
        else:
            print("Please select a valid option")

if __name__ == "__main__":
    main()
