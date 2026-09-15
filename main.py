from database import create_tables, add_student, get_students, search_student
from student import Student


def main():
    create_tables()

    while True:
        print()
        print("Student Management System")
        print()
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print()

        choice = input("Enter your choice: ")

        if choice == "1":
            print()
            print("Add New Student")
            print()

            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            major = input("Enter student major: ")

            student = Student(
                student_id,
                name,
                email,
                major
            )

            add_student(student)

            print()
            print("Student added successfully.")

        elif choice == "2":
            print()
            print("View Students")
            print()

            students = get_students()

            for student in students:
                print(f"ID: {student[0]}")
                print(f"Name: {student[1]}")
                print(f"Email: {student[2]}")
                print(f"Major: {student[3]}")
                print("-" * 30)

        elif choice == "3":
            print()
            print("Search Student")
            print()

            student_id = int(input("Enter student ID: "))

            student = search_student(student_id)

            if student:
                print()
                print(f"ID: {student[0]}")
                print(f"Name: {student[1]}")
                print(f"Email: {student[2]}")
                print(f"Major: {student[3]}")
            else:
                print()
                print("Student not found.")

        elif choice == "4":
            print("Update Student selected.")

        elif choice == "5":
            print("Delete Student selected.")

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()