# ============================================================
# SECTION 1 — WHAT IS A FUNCTION?
# ============================================================

# A function is a reusable block of code that does one specific job.
# Write once, call anywhere, as many times as needed.

# Syntax:
# def function_name(parameters):
#     # code
#     return result

# def       → tells Python you're defining a function
# parameters → inputs the function receives (placeholders)
# return    → what the function gives back

# Parameter vs Argument:
# Parameter → variable in the function definition (placeholder)
# Argument  → actual value passed when calling the function

# def greet(name):        → name is the PARAMETER
#     return f"Hello {name}"
# greet("Kirthivasan")    → "Kirthivasan" is the ARGUMENT


# ============================================================
# SECTION 2 — BASIC FUNCTION
# ============================================================

def greet(name):
    return f"Hello {name}, welcome to your DE journey!"


print(greet("Kirthivasan"))  # Hello Kirthivasan, welcome to your DE journey!
print(greet("Dhoni"))  # Hello Dhoni, welcome to your DE journey!


# ============================================================
# SECTION 3 — MULTIPLE PARAMETERS
# ============================================================

def calculate_average(marks, name):
    average = round(sum(marks) / len(marks), 2)
    return f"{name}'s average: {average}"


print(calculate_average([78, 92, 85, 67, 90], "Arun"))  # Arun's average: 82.4
print(calculate_average([90, 95, 88, 92, 97], "Karthik"))  # Karthik's average: 92.4


# ============================================================
# SECTION 4 — DEFAULT PARAMETERS
# ============================================================

# Default parameters are fallbacks.
# If you provide a value — it uses yours.
# If you don't — it uses the default.

def greet_with_role(name, role="Data Engineer"):
    return f"Hello {name}, future {role}!"


print(greet_with_role("Kirthivasan"))  # uses default role
print(greet_with_role("Kirthivasan", "DE Lead"))  # overrides default


# DE use case — flexible pipeline reader:
# def read_data(file_path, separator=",", encoding="utf-8"):
#     pass
#
# read_data("sales.csv")                        → uses defaults
# read_data("sales.csv", separator=";")         → override separator only
# read_data("sales.csv", encoding="latin-1")    → override encoding only


# ============================================================
# SECTION 5 — MULTIPLE RETURN VALUES
# ============================================================

# Python functions can return multiple values at once
# Returned as a tuple, unpacked into separate variables

def get_stats(marks):
    total = sum(marks)
    average = round(total / len(marks), 2)
    highest = max(marks)
    lowest = min(marks)
    return total, average, highest, lowest  # returns a tuple


total, average, highest, lowest = get_stats([78, 92, 85, 67, 90])
print(f"Total: {total}")  # 412
print(f"Average: {average}")  # 82.4
print(f"Highest: {highest}")  # 92
print(f"Lowest: {lowest}")  # 67


# Note: order of unpacking must match order of return
# return total, average, highest, lowest
# total, average, highest, lowest = get_stats(...)  ← same order


# ============================================================
# SECTION 6 — LAMBDA FUNCTIONS
# ============================================================

# Lambda = mini function written in one line
# Use when: function is simple, used only once, passed as argument

# Syntax:
# lambda parameter: expression
# No def, no function name, no return — returns automatically

# Normal function vs Lambda:
def square_normal(n):
    return n ** 2


square_lambda = lambda n: n ** 2

print(square_normal(5))  # 25
print(square_lambda(5))  # 25 — identical output

# Rule of thumb:
# Simple, one-time use → lambda
# Complex or reused → def function

# Lambda with sorted():
players = ["Dhoni", "Kohli", "Jadeja", "Rohit", "Bumrah"]
sorted_by_length = sorted(players, key=lambda p: len(p))
print(sorted_by_length)  # ['Dhoni', 'Kohli', 'Rohit', 'Jadeja', 'Bumrah']

# Descending order:
sorted_desc = sorted(players, key=lambda p: len(p), reverse=True)
print(sorted_desc)

# Lambda with max():
students = [
    {"name": "Arun", "marks": [78, 92, 85, 67, 90]},
    {"name": "Karthik", "marks": [90, 95, 88, 92, 97]},
    {"name": "Vijay", "marks": [80, 75, 88, 92, 85]}
]

topper = max(students, key=lambda s: sum(s["marks"]) / len(s["marks"]))
print(f"Topper: {topper['name']}")  # Karthik


# Reading lambda:
# lambda s: sum(s["marks"]) / len(s["marks"])
# → "given a student s, calculate their average"


# ============================================================
# SECTION 7 — *args (variable positional arguments)
# ============================================================

# Use when you don't know how many arguments a function will receive
# *args collects all positional arguments into a TUPLE

def add(*args):
    print(args)  # shows the tuple
    return sum(args)


print(add(1, 2))  # (1, 2) → 3
print(add(1, 2, 3))  # (1, 2, 3) → 6
print(add(1, 2, 3, 4, 5))  # (1, 2, 3, 4, 5) → 15


# The * is what matters, not the name 'args'
# *args, *numbers, *values — all valid

# DE use case:
# def process_pipeline(*steps):
#     for step in steps:
#         print(f"Running: {step}")
#
# process_pipeline("extract", "clean", "transform", "load")
# process_pipeline("extract", "load")  → fewer steps, same function


# ============================================================
# SECTION 8 — **kwargs (variable keyword arguments)
# ============================================================

# Use when you want named arguments with key=value pairs
# **kwargs collects all keyword arguments into a DICTIONARY

def player_info(**kwargs):
    print(kwargs)  # shows the dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")


player_info(name="Dhoni", age=42, jersey=7)
# {'name': 'Dhoni', 'age': 42, 'jersey': 7}
# name: Dhoni
# age: 42
# jersey: 7

# *args  → tuple  (positional, no names)
# **kwargs → dict (named, key=value pairs)

# DE use case:
# def connect_database(**kwargs):
#     host = kwargs.get("host", "localhost")
#     port = kwargs.get("port", 5432)
#     database = kwargs.get("database", "mydb")
#     print(f"Connecting to {host}:{port}/{database}")
#
# connect_database(host="aws-rds.amazonaws.com", database="production")


# ============================================================
# SECTION 9 — SCOPE (local vs global variables)
# ============================================================

# Global variable — defined outside all functions, accessible everywhere
# Local variable — defined inside a function, only accessible inside that function

name = "Kirthivasan"  # global


def greet_scope():
    name = "Dhoni"  # local — doesn't affect global
    print(f"Inside function: {name}")  # Dhoni


greet_scope()
print(f"Outside function: {name}")  # Kirthivasan

# When both exist with same name:
# Inside function → local wins
# Outside function → global wins

# Modifying a global variable inside a function:
count = 0


def increment():
    global count  # explicitly tell Python to use global variable
    count += 1


increment()
increment()
print(count)  # 2

# Without 'global' keyword → Python creates a new local variable
# With 'global' keyword → modifies the actual global variable

# DE use case:
# DB_CONNECTION = "aws-rds.amazonaws.com"  # global config
#
# def extract_data():
#     query = "SELECT * FROM orders"       # local — only needed here
#     # uses DB_CONNECTION from global scope


# ============================================================
# SECTION 10 — EXERCISES (solved)
# ============================================================

# Exercise 1 — sort numbers descending
numbers = [4, 2, 9, 1, 7, 3, 8, 5, 6]
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# Exercise 2 — sort products by price
products = [
    {"name": "Laptop", "price": 75000},
    {"name": "Phone", "price": 25000},
    {"name": "Tablet", "price": 35000},
    {"name": "Watch", "price": 15000}
]
sorted_products = sorted(products, key=lambda p: p["price"])
print(sorted_products)