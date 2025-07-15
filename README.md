# Password Generator

A secure, command-line-based password generator that lets users customize the composition of their password — including length, use of uppercase/lowercase letters, digits, and special characters.

## About

This project was created to practice and apply fundamental Python concepts in a real-world use case. It demonstrates user input handling, randomness, string manipulation, conditional logic, and function modularity.  
It runs fully in the terminal and is ideal for beginners looking to explore CLI interactivity and security-related logic.

## Features

- Specify password length (up to 10 characters)
- Toggle inclusion of:
  - Uppercase letters (A–Z)
  - Lowercase letters (a–z)
  - Numbers (0–9)
  - Special characters (!@#... etc.)
- Random generation with guaranteed inclusion of selected character types
- Password strength improves with complexity
- Automatically reshuffles characters for better randomness
- Looping interface for generating multiple passwords in a single session
- User input validation and error handling for smooth experience

## How to Run

Make sure you have Python 3 installed.

```bash
python password_generator.py
```

Follow the prompts in the terminal to select password length and character types.

## Requirements

-  Python 3.x  
(No external libraries needed, uses only `random` and `string` from Python's standard library.)

## Concepts Used
This project helped reinforce the following Python fundamentals:

- Functions and modular programming
- `while` loops and nested loops
- Conditional statements (`if`, `elif`, `else`)
- Built-in libraries: `random`, `string`
- User input and string handling (`input()`, `.strip()`, `.lower()`)
- Exception handling with `try` and `except`
- Dynamic string construction
- List operations and `random.shuffle()`
- Clean command-line interface structure and user flow

## Sample Output

- How many characters do you want your password to be (0-10 characters): 8
- Do you want to include Uppercase letters in your password (y/n): y
- Do you want to include Lowercase letters in your password (y/n): y
- Do you want to include Numbers in your password (y/n): y
- Do you want to include special characters in your password (y/n): n
- Your password is : A7dkM9gf

- Would you like to create another password (y/n): n
- Goodbye!

## Author

Made by Rohit Nair  
GitHub: [Fraze-byte](https://github.com/Fraze-byte)