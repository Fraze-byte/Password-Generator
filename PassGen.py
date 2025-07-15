# -----------------------------
# Password Generator - CLI Version
# Allows users to generate a secure, customizable password.
# Users can choose length (up to 10 characters), and toggle inclusion of:
# uppercase, lowercase, numbers, and special characters.
# Includes validation, retry loops, and ensures at least one character from each selected type.
# -----------------------------

import random
import string

# Entry point of the program
def main():
    while True:
        # Loop to collect valid user preferences
        while True:
            length = length_input()
            use_upper = uppercase_input()
            use_lower = lowercase_input()
            use_num = num_input()
            use_symbols = symbols_input()

            # Ensure at least one type of character is selected
            if use_upper == "y" or use_lower == "y" or use_num == "y" or use_symbols == "y":
                break
            else:
                print("You must at least select one character type for your password.\nPlease try again.")

        # Generate password based on inputs
        password_generator(length, use_upper, use_lower, use_num, use_symbols)

        # Ask user if they want to generate another password
        while True:
            try:
                pass_check = input("Would you like to create another password (y/n): ").strip().lower()
                if pass_check not in ["y", "n"]:
                    raise ValueError("Input should only be 'y' or 'n'")
                break
            except ValueError as e:
                print("Invalid input:", e)

        # Exit loop if user chooses not to generate another
        if pass_check != "y":
            print("Goodbye!")
            break


# -----------------------------
# INPUT FUNCTIONS
# Each function collects and validates user input for a specific option
# -----------------------------

def length_input():
    while True:
        try:
            length = input("How many characters do you want your password to be (minimum 6 characters): ").strip()
            length = int(length)
            if length >=6 and length <= 25:
                return length
            elif length > 10:
                print("Maximum amount of characters allowed is 25")
            else:
                print("Password length cannot be less than 6")
        except ValueError:
            print("Please enter a numeric value")


def uppercase_input():
    while True:
        try:
            use_upper = input("Do you want to include Uppercase letters in your password (y/n): ").strip().lower()
            if use_upper not in ["y", "n"]:
                raise ValueError("Input must be 'y' or 'n'")
            return use_upper
        except ValueError as e:
            print("Invalid input:", e)


def lowercase_input():
    while True:
        try:
            use_lower = input("Do you want to include Lowercase letters in your password (y/n): ").strip().lower()
            if use_lower not in ["y", "n"]:
                raise ValueError("Input must be 'y' or 'n'")
            return use_lower
        except ValueError as e:
            print("Invalid input:", e)


def num_input():
    while True:
        try:
            use_num = input("Do you want to include Numbers in your password (y/n): ").strip().lower()
            if use_num not in ["y", "n"]:
                raise ValueError("Input must be 'y' or 'n'")
            return use_num
        except ValueError as e:
            print("Invalid input:", e)


def symbols_input():
    while True:
        try:
            use_symbols = input("Do you want to include special characters in your password (y/n): ").strip().lower()
            if use_symbols not in ["y", "n"]:
                raise ValueError("Input must be 'y' or 'n'")
            return use_symbols
        except ValueError as e:
            print("Invalid input:", e)


# -----------------------------
# PASSWORD GENERATION FUNCTION
# Builds a password based on selected options.
# Ensures one character from each selected type is guaranteed.
# -----------------------------

def password_generator(length, use_upper, use_lower, use_num, use_symbols):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    num = string.digits
    symbols = string.punctuation

    guaranteed = []  # Will store at least one guaranteed char from each chosen set
    pool = ""        # Full pool of possible characters to choose from

    # Add required character types
    if use_upper == "y":
        guaranteed.append(random.choice(uppercase))
        pool += uppercase

    if use_lower == "y":
        guaranteed.append(random.choice(lowercase))
        pool += lowercase

    if use_num == "y":
        guaranteed.append(random.choice(num))
        pool += num

    if use_symbols == "y":
        guaranteed.append(random.choice(symbols))
        pool += symbols

    # Fill the remaining password length with random characters from the pool
    remaining_length = length - len(guaranteed)
    for _ in range(remaining_length):
        guaranteed.append(random.choice(pool))

    # Shuffle to avoid predictable patterns
    random.shuffle(guaranteed)
    password = "".join(guaranteed)

    print("Your password is:", password)


# This ensures that `main()` only runs when the script is executed directly,
# and not when imported as a module in another file.
if __name__ == "__main__":
    main()
