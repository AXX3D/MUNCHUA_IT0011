import os

students = []
filename = None

while True:
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
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        filename = input("Enter filename: ").strip()
        if not os.path.exists(filename):
            print("File not found.")
        else:
            with open(filename, "r") as f:
                students = []
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) != 5:  # Ensures the correct number of values
                        print(f"Skipping invalid line: {line.strip()}")
                        continue
                    
                    student_id, first_name, last_name, class_standing, exam = parts
                    try:
                        students.append((student_id, (first_name, last_name), float(class_standing), float(exam)))
                    except ValueError:
                        print(f"Skipping invalid numeric values in line: {line.strip()}")
            print("File loaded successfully.")

    elif choice == "2":
        if filename is None:
            filename = input("Enter filename to save as: ").strip()
        with open(filename, "w") as f:
            for student in students:
                f.write(",".join(map(str, student[0:2] + student[2:])) + "\n")
        print("File saved successfully.")

    elif choice == "3":
        filename = input("Enter filename to save as: ").strip()
        with open(filename, "w") as f:
            for student in students:
                f.write(",".join(map(str, student[0:2] + student[2:])) + "\n")
        print("File saved successfully.")

    elif choice == "4":
        if not students:
            print("No records found.")
        else:
            for student in students:
                print(f"ID: {student[0]} | Name: {student[1][0]} {student[1][1]} | Class Standing: {student[2]} | Exam: {student[3]}")

    elif choice == "5":
        students.sort(key=lambda s: s[1][1])
        print("Records sorted by last name.")

    elif choice == "6":
        students.sort(key=lambda s: (s[2] * 0.6 + s[3] * 0.4), reverse=True)
        print("Records sorted by grade.")

    elif choice == "7":
        student_id = input("Enter Student ID to search: ").strip()
        found = False
        for student in students:
            if student[0] == student_id:
                print(f"Found: {student}")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "8":
        student_id = input("Enter Student ID (6 digits): ").strip()
        if len(student_id) != 6 or not student_id.isdigit():
            print("Invalid ID. Must be a 6-digit number.")
        else:
            first_name = input("Enter First Name: ").strip()
            last_name = input("Enter Last Name: ").strip()
            try:
                class_standing = float(input("Enter Class Standing Grade: ").strip())
                major_exam = float(input("Enter Major Exam Grade: ").strip())
                students.append((student_id, (first_name, last_name), class_standing, major_exam))
                print("Record added.")
            except ValueError:
                print("Invalid grade input. Must be a number.")

    elif choice == "9":
        student_id = input("Enter Student ID to edit: ").strip()
        for i in range(len(students)):
            if students[i][0] == student_id:
                try:
                    class_standing = input(f"Enter New Class Standing Grade ({students[i][2]}): ").strip()
                    major_exam = input(f"Enter New Major Exam Grade ({students[i][3]}): ").strip()

                    class_standing = float(class_standing) if class_standing else students[i][2]
                    major_exam = float(major_exam) if major_exam else students[i][3]

                    students[i] = (students[i][0], students[i][1], class_standing, major_exam)
                    print("Record updated.")
                except ValueError:
                    print("Invalid grade input. Must be a number.")
                break
        else:
            print("Student not found.")

    elif choice == "10":
        student_id = input("Enter Student ID to delete: ").strip()
        students = [s for s in students if s[0] != student_id]
        print("Record deleted.")

    elif choice == "11":
        break

    else:
        print("Invalid choice. Try again.")
