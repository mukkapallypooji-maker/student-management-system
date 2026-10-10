students = []
#adding student details
def add_student():
    student_number = int(input("Enter student number: "))
    student_name = input("Enter student name: ")
    student_age = int(input("Enter student age: "))
    branch = input("Enter branch: ")

    student = {
        "num": student_number,
        "name": student_name,
        "age": student_age,
        "branch": branch
    }

    students.append(student)
    print("Student added successfully")

#displaying students
def display_students():
    if len(students) == 0:
        print("No students found")
    else:
        for student in students:
            print("Number:", student["num"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            print("------------------")

#searching for the student
def search_student():
    student_number = int(input("Enter student number to search: "))

    found = False

    for student in students:
        if student_number == student["num"]:
            print("Student found")
            print("Number:", student["num"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Branch:", student["branch"])
            found = True
            break

    if found == False:
        print("Student not found")

#updating the student
def update_student():
    student_number = int(input("Enter student number to update: "))

    found = False

    for student in students:
        if student_number == student["num"]:
            new_name = input("Enter new name: ")
            student["name"] = new_name

            new_age = int(input("Enter new age: "))
            student["age"] = new_age

            new_branch = input("Enter new branch: ")
            student["branch"] = new_branch

            found = True
            print("Student updated successfully")
            break

    if found == False:
        print("Student not found")

#delete the students
def delete_student():
    student_number = int(input("Enter student number to delete: "))

    found = False

    for student in students:
        if student_number == student["num"]:
            students.remove(student)
            found = True
            print("Student deleted successfully")
            break

    if found == False:
        print("Student not found")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice")