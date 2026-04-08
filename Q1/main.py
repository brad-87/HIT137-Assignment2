import os

def read_file(filename):
    # Format the file path to be the full system path
    path = os.path.join(os.path.dirname(__file__), filename)
    # Open specified file, read the file and return the contents as a string
    with open(path, "r") as file:
        return file.read()

def validate_int_input(prompt):
    while True:
        try:
            # Prompt user for input
            user_value = int(input(prompt))
            return user_value
        except ValueError:
            # If the entered input wasn't an integer, notify user for valid input
            print("Invalid value. Please enter an integer value")




def main():
    # Read 'raw_text.txt' and store data into raw_input string
    raw_input = read_file("raw_text.txt")

    # Get shift values from user and validate input
    shift1 = validate_int_input("Enter shift 1: ")
    shift2 = validate_int_input("Enter shift 2: ")

    # for testing only
    print(raw_input)
    print(shift1)
    print(shift2)


main()
