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

def encrypt_char(c, shift1, shift2):
    # Encrypt a single character

    # Lowercase letters from a–m , shift forward by shift1 * shift2
    if 'a' <= c <= 'm':
        return chr((ord(c) - ord('a') + shift1 * shift2) % 26 + ord('a'))

    # Lowercase letters from n–z , shift backward by (shift1 + shift2)
    elif 'n' <= c <= 'z':
        return chr((ord(c) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))

    # Uppercase letters from A–M , shift backward by shift1
    elif 'A' <= c <= 'M':
        return chr((ord(c) - ord('A') - shift1) % 26 + ord('A'))

    # Uppercase letters from N–Z , shift forward by (shift2 squared)
    elif 'N' <= c <= 'Z':
        return chr((ord(c) - ord('A') + (shift2 ** 2)) % 26 + ord('A'))

    # Any other characters (spaces, punctuation) remain unchanged
    else:
        return c


def encrypt_text(text, shift1, shift2):
    # Go through the entire text and encrypt each character
    encrypted = ""

    for c in text:
        encrypted += encrypt_char(c, shift1, shift2)

    return encrypted


def write_file(filename, content):
    # Create full file path
    path = os.path.join(os.path.dirname(__file__), filename)

    # Write the encrypted content into a new file
    with open(path, "w") as file:
        file.write(content)


def main():
    # Read 'raw_text.txt' and store data into raw_input string
    raw_input = read_file("raw_text.txt")

    # Get shift values from user and validate input
    shift1 = validate_int_input("Enter shift 1: ")
    shift2 = validate_int_input("Enter shift 2: ")

     # Encrypt the original text using the given shift values
    encrypted_text = encrypt_text(raw_input, shift1, shift2)

    # Save the encrypted result into a new file
    write_file("encrypted_text.txt", encrypted_text)

    # Inform user that encryption is complete
    print("Encryption complete. Check encrypted_text.txt")


    # for testing only
    print(raw_input)
    print(shift1)
    print(shift2)


main()
