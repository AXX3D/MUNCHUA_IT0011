last_name = input("Enter Last Name: ")
first_name = input("Enter First Name: ")
age = input("Enter Age: ")
contact_number = input("Enter Contact Number: ")
course = input("Enter Course: ")

formatted = (f"Last Name: {last_name}\n"
                   f"First Name: {first_name}\n"
                   f"Age: {age}\n"
                   f"Contact Number: {contact_number}\n"
                   f"Course: {course}\n\n")

with open("students.txt", "a") as file:
    file.write(formatted)

print("Student Information has been saved to 'students.txt'")
