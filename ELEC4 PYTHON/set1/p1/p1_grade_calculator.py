# Name: JENELLE M. SABAL
# Section: IV-BSIT C
# Activity: P1 - Student Grade Calculator
# Date: November 20, 2026

PASSING_AVERAGE = 75

def get_student_grades():
    grades = []

    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))

            if number_of_grades > 0:
                break
            else:
                print("Please enter at least 1 grade.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    print("\nGrades successfully entered!")
    return grades


def calculate_average(grades):
    return sum(grades) / len(grades)

# Function 3: Get the highest grade
def get_highest_grade(grades):
    return max(grades)

# Function 4: Get the lowest grade
def get_lowest_grade(grades):
    return min(grades)

# Function 5: Determine pass or fail
def determine_status(grades):
    average = calculate_average(grades)

    if average >= PASSING_AVERAGE:
        return "PASSED"
    else:
        return "FAILED"

# Function 6: Display the grade results
def display_results(grades):
    if not grades:
        print("\nNo grades available. Please enter grades first.")
        return

    average = calculate_average(grades)
    highest = get_highest_grade(grades)
    lowest = get_lowest_grade(grades)
    status = determine_status(grades)

    print("\n========== GRADE RESULTS ==========")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")
    print(f"Status: {status}")
    print("===================================")

# Main function: Controls the program menu
def main():
    grades = []

    print("===================================")
    print("   STUDENT GRADE CALCULATOR")
    print("   Student: JENELLE M. SABAL")
    print("   Section: IV-BSIT C")
    print("===================================")

    while True:
        print("\n========== MAIN MENU ==========")
        print("[1] Enter Student Grades")
        print("[2] View Grade Results")
        print("[3] Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            grades = get_student_grades()

        elif choice == "2":
            display_results(grades)

        elif choice == "3":
            print("\nThank you for using the Grade Calculator!")
            print("Program ended.")
            break

        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")

# Run the main function
if __name__ == "__main__":
    main()

# Explanation:
# A global variable is declared outside all functions and can be accessed
# throughout the program. In this program, PASSING_AVERAGE is a global
# variable because it is declared outside the functions and is used to
# determine whether the student's average is passing or failing.
# The grades variable inside main() is a local variable because it is
# created inside that function and belongs to its local scope.