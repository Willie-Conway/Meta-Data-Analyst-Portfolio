# Python Syntax and Dot Notation Reference

# 1. Whitespace and Indentation
# In Python, indentation is critical as it defines blocks of code.
# Here's a simple example of an if-else statement with proper indentation.

score = 85  # Example score variable

if score >= 80:
    print("You passed!")  # This line is indented to indicate it belongs to the if block
else:
    print("Please try again.")  # This line belongs to the else block

# 2. Variables
# Variables hold values and do not require explicit data type declarations.

grade_average = 89.5  # Float
name = "Alice"        # String
age = 25              # Integer
is_new_student = True  # Boolean

# 3. Comments
# Comments explain code and are ignored by the interpreter.

# This is a single-line comment.

"""
This is a multi-line comment.
It can span multiple lines.
"""

# 4. Lists
# Lists store sequences of items and are mutable.

shopping_list = ["milk", "eggs", "bread"]  # List of items
my_numbers = [1, 5, 3, 9]                   # List of numbers

# Accessing elements in a list (zero-indexed)
print(my_numbers[0])  # Output: 1 (first element)
print(shopping_list[2])  # Output: bread (third element)

# Common list operations
my_numbers.append(7)  # Adds 7 to the end of my_numbers
print(my_numbers)     # Output: [1, 5, 3, 9, 7]

my_numbers.insert(1, 4)  # Inserts 4 at index 1
print(my_numbers)         # Output: [1, 4, 5, 3, 9, 7]

my_numbers.remove(3)      # Removes the first occurrence of 3
print(my_numbers)         # Output: [1, 4, 5, 9, 7]

# 5. Dictionaries
# Dictionaries store unordered collections of key-value pairs.

student_info = {
    "name": "Bob",
    "age": 22,
    "major": "Computer Science"
}

# Accessing a value using its key
print(student_info["name"])  # Output: Bob

# Common dictionary operations
student_info["GPA"] = 3.8  # Adds a new key-value pair for GPA
print(student_info)         # Output: {'name': 'Bob', 'age': 22, 'major': 'Computer Science', 'GPA': 3.8}

del student_info["age"]    # Removes the key-value pair with the key 'age'
print(student_info)         # Output: {'name': 'Bob', 'major': 'Computer Science', 'GPA': 3.8}
