namel = input("Enter Last Name: ")
namef = input("Enter First Name: ")
age = input("Enter Age: ")
contact = input("Enter Contact Number: ")
course = input("Enter Course: ")

formatted = (f"Last Name: {namel}\n"
                   f"First Name: {namef}\n"
                   f"Age: {age}\n"
                   f"Contact Number: {contact}\n"
                   f"Course: {course}\n\n")

with open("students.txt", "a") as file:
    file.write(formatted)

print("Student Information has been saved to 'students.txt'")
