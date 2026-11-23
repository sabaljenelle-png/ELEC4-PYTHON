# Name: JENELLE M. SABAL
# Section: IV-BSIT C
# Activity: P2 - Custom Module: student_utils
# Date: November 20, 2026

# Import the entire custom module
import student_utils

# Import a specific function from the custom module
from student_utils import calculate_average

# Import a built-in Python module
import datetime

# Function to accept student grades
def get_student_grades():
    grades = []

    # Ask how many grades the user wants to enter
    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))

            if number_of_grades > 0:
                break
            else:
                print("Please enter at least 1 grade.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Accept and validate each grade
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

    return grades

# Main program
def main():
    print("======================================")
    print("       STUDENT GRADE REPORT")
    print("       Student: JENELLE M. SABAL")
    print("       Section: IV-BSIT C")
    print("======================================")

    # Get grades from the user
    grades = get_student_grades()

    # Use the imported functions
    average = calculate_average(grades)
    status = student_utils.determine_status(grades)
    highest = student_utils.get_highest_grade(grades)
    lowest = student_utils.get_lowest_grade(grades)

    # Get the current date and time using datetime
    report_date = datetime.datetime.now()

    # Display the results
    print("\n========== GRADE RESULTS ==========")
    print(f"Grades: {grades}")
    print(f"Average: {average:.2f}")
    print(f"Highest Grade: {highest}")
    print(f"Lowest Grade: {lowest}")
    print(f"Status: {status}")
    print("===================================")

    print("\nReport generated on:")
    print(report_date.strftime("%B %d, %Y - %I:%M %p"))

    print("\nThank you for using the program!")

# Run the main program
if __name__ == "__main__":
    main()