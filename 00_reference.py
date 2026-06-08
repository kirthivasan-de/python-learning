# ============================================================
# KIRTHIVASAN | DATA ENGINEERING JOURNEY | JUNE 2026
# 00_REFERENCE — MASTER CHEATSHEET
# Quick reference for all syntax, methods, and DE notes
# ============================================================


# ============================================================
# SECTION 1 — DATA TYPES
# ============================================================

# str   → text                  name = "Kirthivasan"
# int   → whole number          age = 26
# float → decimal number        height = 6.2
# bool  → True or False         is_csk_fan = True
# list  → ordered collection    players = ["Dhoni", "Kohli"]
# dict  → key-value pairs       person = {"name": "Kirthivasan"}  # covered in 03
# tuple → immutable list        coords = (10, 20)                 # covered later
# None  → no value              value = None

# Check type of any variable
# type(variable)


# ============================================================
# SECTION 2 — TYPE CONVERSION
# ============================================================

# int("26")       → 26       string to integer
# float("6.2")    → 6.2      string to float
# str(26)         → "26"     integer to string
# bool(0)         → False    0 is False, anything else is True
# bool(1)         → True

# Common DE use case — fix columns read as wrong type from CSV
# df["age"] = df["age"].astype(int)       # pandas version of int()
# df["price"] = df["price"].astype(float) # pandas version of float()


# ============================================================
# SECTION 3 — F-STRINGS
# ============================================================

# Basic
# f"{variable}"

# Expression inside
# f"{2026 - age}"

# Two decimal places
# f"{price:.2f}"

# Dynamic SQL query
# f"SELECT * FROM orders WHERE year = {current_year - 1}"

# Patterns:
# f"{name} is {age} years old"
# f"Player {index + 1}: {player}"
# f"{value:.2f}"                    → 2 decimal places
# f"{value:,}"                      → thousands separator e.g. 1,000,000


# ============================================================
# SECTION 4 — STRING METHODS
# ============================================================

# .upper()        → "dhoni"       → "DHONI"         all caps
# .lower()        → "DHONI"       → "dhoni"         all lowercase
# .capitalize()   → "dhoni"       → "Dhoni"         first letter only
# .title()        → "ms dhoni"    → "Ms Dhoni"      every word capitalized
# .strip()        → " dhoni "     → "dhoni"         remove whitespace
# .lstrip()       →               →                 remove left whitespace
# .rstrip()       →               →                 remove right whitespace
# .replace(a, b)  → replace a with b in string
# .split(",")     → split string into list by delimiter
# .join(list)     → join list into string
# len(string)     → count characters

# DE use cases:
# .strip()    → clean extra spaces from CSV data
# .lower()    → normalize casing before comparing
# .replace()  → fix inconsistent values e.g. "N/A" → ""
# .split()    → split comma-separated values in a column


# ============================================================
# SECTION 5 — ARITHMETIC OPERATORS
# ============================================================

# +    addition               5 + 3 = 8
# -    subtraction            5 - 3 = 2
# *    multiplication         5 * 3 = 15
#      (also string repeat)   "ab" * 3 = "ababab"
# /    division               10 / 3 = 3.333  (always float)
# //   floor division         10 // 3 = 3     (integer result)
# %    modulo (remainder)     10 % 3 = 1
# **   power                  2 ** 3 = 8

# DE use cases:
# %    check even/odd         n % 2 == 0 → even
# //   batch processing       row_count // batch_size
# **   squaring, scaling      value ** 2


# ============================================================
# SECTION 6 — COMPARISON OPERATORS
# ============================================================

# ==   equal to               age == 26
# !=   not equal to           status != "failed"
# >    greater than           score > 70
# <    less than              price < 100
# >=   greater than or equal  age >= 18
# <=   less than or equal     discount <= 0.5


# ============================================================
# SECTION 7 — LOGICAL OPERATORS
# ============================================================

# and  → both conditions true     age > 18 and age < 60
# or   → at least one true        status == "pass" or score > 80
# not  → reverse condition        not is_null


# ============================================================
# SECTION 8 — LIST METHODS
# ============================================================

# Creation
# players = ["Dhoni", "Kohli", "Jadeja"]

# Adding
# players.append("Hardik")          → add to end
# players.insert(1, "Virat")        → add at index 1

# Removing
# players.remove("Rohit")           → remove by value
# players.pop(0)                    → remove by index, returns value
# players.pop()                     → remove last element

# Modifying
# players[0] = "Gill"               → replace by index

# Info
# len(players)                      → count of elements
# players.count("Dhoni")            → how many times value appears
# players.index("Kohli")            → index of value
# "Dhoni" in players                → True/False existence check

# Sorting
# players.sort()                    → sort in place (alphabetical)
# players.sort(reverse=True)        → reverse sort
# sorted(players)                   → returns new sorted list

# Combining
# players + ["Hardik", "Bumrah"]    → merge two lists
# players * 2                       → repeat list


# ============================================================
# SECTION 9 — LIST INDEXING AND SLICING
# ============================================================

# Indexing
# list[0]     → first element
# list[-1]    → last element
# list[-2]    → second from last

# Slicing syntax: list[start : end : step]
# start → included
# end   → EXCLUDED (always one step ahead of what you want)
# step  → how many positions to jump

# Examples
# list[1:3]   → index 1 and 2 (NOT 3)
# list[:3]    → first 3 elements
# list[2:]    → index 2 to end
# list[-2:]   → last 2 elements
# list[::2]   → every 2nd element (forward)
# list[::-1]  → entire list reversed
# list[::-2]  → every 2nd element (backward)

# Step rules:
# Positive step → forward
# Negative step → backward


# ============================================================
# SECTION 10 — LIST COMPREHENSION
# ============================================================

# Patterns:
# [expression for item in list]                          → transform
# [item for item in list if condition]                   → filter
# [expression for item in list if condition]             → transform + filter

# Examples:
# [player.upper() for player in players]
# [player for player in players if len(player) > 5]
# [n ** 2 for n in numbers if n % 2 == 0]
# [f"{n} is odd" for n in numbers if n % 2 != 0]
# [(celsius * 9/5) + 32 for celsius in temperatures]


# ============================================================
# SECTION 11 — LOOPS
# ============================================================

# Simple loop
# for item in list:
#     print(item)

# Enumerate — index + value
# for index, item in enumerate(list):
#     print(index, item)

# Range loop
# for i in range(5):        → 0, 1, 2, 3, 4
# for i in range(1, 6):     → 1, 2, 3, 4, 5
# for i in range(0, 10, 2): → 0, 2, 4, 6, 8

# While loop
# while condition:
#     do something


# ============================================================
# SECTION 12 — USEFUL BUILT-IN FUNCTIONS
# ============================================================

# type(x)       → data type of x
# len(x)        → length of string, list, dict
# int(x)        → convert to integer
# float(x)      → convert to float
# str(x)        → convert to string
# bool(x)       → convert to boolean
# print(x)      → output to console
# input(x)      → take user input
# range(n)      → generate sequence of numbers
# enumerate(x)  → add index to iterable
# sorted(x)     → return sorted version
# sum(x)        → sum of list
# min(x)        → minimum value
# max(x)        → maximum value
# abs(x)        → absolute value
# round(x, n)   → round to n decimal places


# ============================================================
# SECTION 13 — DE CONNECTION NOTES
# ============================================================

# type()        → check column types when reading CSV
# int()         → fix numeric columns stored as strings
# float()       → fix decimal columns stored as strings
# .upper/lower  → normalize inconsistent casing in data
# .strip()      → remove extra whitespace from values
# len()         → validate string lengths
# list comp     → transform and filter rows efficiently
# enumerate()   → iterate with row numbers
# % operator    → check even/odd, batch sizing
# f-strings     → dynamic SQL query building, file paths, logging

# Dynamic SQL example:
# current_year = 2026
# query = f"SELECT * FROM orders WHERE year = {current_year - 1}"
# → SELECT * FROM orders WHERE year = 2025

# File path example:
# file_name = f"report_{2026}_{month}.csv"

# Pandas type fixing (preview — covered in Month 1 Week 3):
# df["age"] = df["age"].astype(int)
# df["name"] = df["name"].str.strip().str.lower()


# ============================================================
# SECTION 14 - DICTIONARIES
# ============================================================

# Creation          dict = {"key": value}
# Access            dict["key"]
# Add               dict["new_key"] = value
# Update            dict["existing_key"] = new_value
# Delete            del dict["key"]
# Safe delete       dict.pop("key")          → returns value
# All keys          dict.keys()
# All values        dict.values()
# All pairs         dict.items()
# Key exists        "key" in dict            → True/False
# Length            len(dict)
# Nested access     dict["outer"]["inner"]
# Loop              for key, value in dict.items()

# ============================================================
# SECTION 14 — FUNCTIONS
# ============================================================

# Basic function         def name(params): return value
# Default parameter      def name(param="default"):
# Multiple return        return a, b, c → a, b, c = func()
# Lambda                 lambda param: expression
# *args                  collects positional args → tuple
# **kwargs               collects keyword args → dict
# Local variable         defined inside function, dies after
# Global variable        defined outside, lives everywhere
# global keyword         use inside function to modify global var

# When to use lambda vs def:
# lambda → simple, one-line, used once, passed as argument
# def    → complex, multi-line, reused multiple times

# *args vs **kwargs:
# *args   → unknown number of values      add(1, 2, 3)
# **kwargs → unknown number of key=value  info(name="Dhoni", age=42)


# ============================================================
# UPCOMING SECTIONS (TO BE ADDED AFTER EACH TOPIC)
# ============================================================

# SECTION 15 — FUNCTIONS             (04_functions.py)
# SECTION 16 — ERROR HANDLING        (05_error_handling.py)
# SECTION 17 — FILE HANDLING         (06_file_handling.py)
# SECTION 18 — PANDAS BASICS         (07_pandas_basics.py)
# SECTION 19 — PANDAS DATA CLEANING  (08_pandas_cleaning.py)
# SECTION 20 — SQL PATTERNS          (added in Month 2)
# SECTION 21 — PYSPARK SNIPPETS      (added in Month 3)
# SECTION 22 — DBT PATTERNS          (added in Month 4)