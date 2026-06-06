# ================================================================
# KIRTHIVASAN | DATA ENGINEERING JOURNEY | JUNE 2026
# ================================================================


# ================================================================
# SECTION 1 - VARIABLES AND DATA TYPES
# ================================================================

# Basic variable declaration
name = "Kirthivasan"
age = 26
height = 6.2
is_csk_fan = True
bike = "Honda CB350"

# Checking types with type()
print(type(name))         # <class 'str'>
print(type(age))          # <class 'str'>
print(type(height))       # <class 'str'>
print(type(is_csk_fan))   # <class 'str'>
print(type(bike))         # <class 'str'>

# ================================================================
# SECTION 2 - F-STRINGS
# ================================================================

# Basic f-string
print(f"{name} is {age} years old")

# Expression inside f-string
print(f"Full name: {name}, Age: {age}, Born in: {2026 - age}")

# Multiple variables in one f-string
print(f"{name} is {age} years old, standing at {height} feet tall, is a CSK fan: {is_csk_fan} and has a {bike} bike")

# ================================================================
# SECTION 3 - FORMAT VERBS (printf style)
# ================================================================

# %s = string, %d = integer, %f = float, %t = boolean, %T = type
print("%s is %d years old" % (name, age))
print(f"Engine size: %.2f cc" % 349.55)  # .2f = 2 decimal places

# ================================================================
# SECTION 4 - TYPE CONVERSION
# ================================================================

# string to int
print(int("26") + 50)  # 76

# string to float
print(float("26") + 50)  # 76.0

# int to string (concatenation)
print(str(26) + "50")  # 2650

# Common type conversions
int("100")  # string → integer
float("6.2")  # string → float
str(26)  # integer → string

# TypeError example — mixing incompatible types
# print("26" + 26)  # This throws TypeError — uncomment to see

# String repetition (not multiplication)
print("499.99" * 5)  # 499.99499.99499.99499.99499.99