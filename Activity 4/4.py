import os

students = []
filename = None

def menu():
    print("\nSTUDENT RECORD MANAGEMENT")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All")
    print("5. Sort by Last Name")
    print("6. Sort by Grade")
    print("7. Find Student")
    print("8. Add Student")
    print("9. Edit Student")
    print("10. Delete Student")
    print("11. Exit")

def open_file():
    global filename, students
    filename = input("Enter filename: ")
    if not os.path.exists(filename):
        print("File not found.")
        return
    with open(filename, "r") as f:
        students = [tuple(line.strip().split(",")) for line in f]
        students = [(s[0], (s[1], s[2]), float(s[3]), float(s[4])) for s in students]
    print("File loaded successfully.")

def save():
    if filename is None:
        save_as()
    else:
        with open(filename, "w") as f:
            for student in students:
                f.write(",".join(map(str, student[0:2] + student[2:])) + "\n")
        print("File saved successfully.")

def save_as():
    global filename
    filename = input("Enter filename to save as: ")
    save()

def show_all():
    if not students:
        print("No records found.")
    else:
        for student in students:
            print(f"ID: {student[0]} | Name: {student[1][0]} {student[1][1]} | Class Standing: {student[2]} | Exam: {student[3]}")

def sort_last_name():
    global students
    students.sort(key=lambda s: s[1][1])
    print("Records sorted by last name.")

def sort_grade():
    global students
    students.sort(key=lambda s: (s[2] * 0.6 + s[3] * 0.4), reverse=True)
    print("Records sorted by grade.")

def find_student():
    student_id = input("Enter Student ID to search: ")
    for student in students:
        if student[0] == student_id:
            print(f"Found: {student}")
            return
    print("Student not found.")

def add_student():
    student_id = input("Enter Student ID (6 digits): ")
    if len(student_id) != 6 or not student_id.isdigit():
        print("Invalid ID. Must be a 6-digit number.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    students.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added.")

def edit_student():
    student_id = input("Enter Student ID to edit: ")
    for i, student in enumerate(students):
        if student[0] == student_id:
            class_standing = float(input(f"Enter New Class Standing Grade ({student[2]}): ") or student[2])
            major_exam = float(input(f"Enter New Major Exam Grade ({student[3]}): ") or student[3])
            students[i] = (student[0], student[1], class_standing, major_exam)
            print("Record updated.")
            return
    print("Student not found.")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    global students
    students = [s for s in students if s[0] != student_id]
    print("Record deleted.")

while True:
    menu()
    choice = input("Enter choice: ")
    if choice == "1":
        open_file()
    elif choice == "2":
        save()
    elif choice == "3":
        save_as()
    elif choice == "4":
        show_all()
    elif choice == "5":
        sort_last_name()
    elif choice == "6":
        sort_grade()
    elif choice == "7":
        find_student()
    elif choice == "8":
        add_student()
    elif choice == "9":
        edit_student()
    elif choice == "10":
        delete_student()
    elif choice == "11":
        break
    else:
        print("Invalid choice. Try again.")
