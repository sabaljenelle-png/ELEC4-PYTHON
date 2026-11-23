# Name: JENELLE M. SABAL
# Section: IV-BSIT C
# Activity: P4 - Safe Menu Program
# Date: November 20, 2026


def divide_numbers():
    print("\n========== DIVISION ==========")

    try:
        # Ask the user to enter two numbers
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        # Perform division
        result = number1 / number2

    except ValueError:
        # This happens when the user enters letters or invalid numbers
        print("Error: Please enter valid numeric values.")

    except ZeroDivisionError:
        # This happens when the second number is zero
        print("Error: Division by zero is not allowed.")

    else:
        # This runs only when no exception occurs
        print(f"Result: {number1} / {number2} = {result}")

    finally:
        # This runs whether an error occurs or not
        print("Division operation finished.")


def open_file():
    print("\n========== OPEN FILE ==========")

    filename = input("Enter the file name: ").strip()

    try:
        # Open the file in read mode
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()

    except FileNotFoundError:
        # This happens when the requested file does not exist
        print(f"Error: The file '{filename}' was not found.")

    else:
        # This runs when the file opens successfully
        print("\nFile Contents:")
        if contents:
            print(contents)
        else:
            print("The file is empty.")

    finally:
        # This runs whether the file exists or not
        print("File operation finished.")


def display_menu():
    print("\n========== SAFE MENU PROGRAM ==========")
    print("[1] Divide Two Numbers")
    print("[2] Open and Read a File")
    print("[3] Exit")
    print("=======================================")


def main():
    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("\nThank you for using the Safe Menu Program!")
            print("Program ended.")
            break

        else:
            print("\nInvalid menu choice!")
            print("Please select only 1, 2, or 3.")


if __name__ == "__main__":
    main()
