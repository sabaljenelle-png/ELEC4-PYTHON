# Name: JENELLE M. SABAL
# Section: IV-BSIT C
# Activity: P3 - Student Record Manager
# Date: November 20, 2026

# List to store student names
students = []

# Set to prevent duplicate student names
student_names = set()

# Function 1: Add a student
def add_student(students, student_names):
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

    # Convert the name to lowercase for comparison
    normalized_name = name.casefold()

    if normalized_name in student_names:
        print("Student already exists! Duplicate entry prevented.")
    else:
        students.append(name)
        student_names.add(normalized_name)
        print(f"\n{name} has been successfully added!")

# Function 2: Remove a student
def remove_student(students, student_names):
    name = input("Enter the student name to remove: ").strip()

    normalized_name = name.casefold()

    for student in students:
        if student.casefold() == normalized_name:
            students.remove(student)
            student_names.remove(normalized_name)
            print(f"\n{student} has been successfully removed!")
            return

    print("Student not found!")

# Function 3: Search for a student
def search_student(students):
    search_name = input("Enter student name to search: ").strip()

    if not search_name:
        print("Please enter a name to search.")
        return

    search_name = search_name.casefold()

    found_students = []

    for student in students:
        if search_name in student.casefold():
            found_students.append(student)

    if found_students:
        print("\nSearch Results:")
        for student in found_students:
            print(f"- {student}")
    else:
        print("No matching student found!")

# Function 4: Display all students
def display_students(students):
    if not students:
        print("\nNo students in the record yet.")
        return

    # Sort names alphabetically without case sensitivity
    sorted_students = sorted(students, key=str.casefold)

    print("\n========== STUDENT LIST ==========")

    for number, student in enumerate(sorted_students, start=1):
        print(f"{number}. {student}")

    print("----------------------------------")
    print(f"Total Students: {len(students)}")
    print("==================================")

# Main function: Controls the program menu
def main():
    print("=================================")
    print("      STUDENT RECORD MANAGER")
    print("      Section: IV-BSIT C")
    print("=================================")

    while True:
        print("\n========== MAIN MENU ==========")
        print("[1] Add Student")
        print("[2] Remove Student")
        print("[3] Search Student")
        print("[4] Display All Students")
        print("[5] Exit")
        print("===============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students, student_names)

        elif choice == "2":
            remove_student(students, student_names)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            display_students(students)

        elif choice == "5":
            print("\nThank you for using Student Record Manager!")
            print("Program ended.")
            break

        else:
            print("\nInvalid choice! Please select 1 to 5.")

# Run the main function
if __name__ == "__main__":
    main()

# Explanation of Lists and Sets:
# A list is a collection that maintains insertion order and allows duplicate
# values. A set is a collection that stores only unique values and does not
# guarantee insertion order. In this program, I used a list named students
# to store and display the student names. I also used a set named
# student_names to prevent duplicate entries by comparing names without
# considering uppercase and lowercase letters.