
# Name: JENELLE M. SABAL
# Section: IV-BSIT C
# Activity: P2 - Custom Module: student_utils
# Date: November 20, 2026

# Global variable for the passing average
PASSING_AVERAGE = 75

# Function 1: Calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function 2: Determine pass or fail
def determine_status(grades):
    average = calculate_average(grades)

    if average >= PASSING_AVERAGE:
        return "PASSED"
    else:
        return "FAILED"

# Function 3: Get the highest grade
def get_highest_grade(grades):
    return max(grades)

# Function 4: Get the lowest grade
def get_lowest_grade(grades):
    return min(grades)