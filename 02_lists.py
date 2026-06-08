# ============================================================
# SECTION 1 — LISTS
# ============================================================

players = ["Dhoni", "Kohli", "Jadeja", "Rohit", "Bumrah"]

# Basic operations
print(players)  # full list
print(type(players))  # <class 'list'>
print(len(players))  # 5

# --- INDEXING ---
print(players[0])  # Dhoni  — first element
print(players[1])  # Kohli
print(players[4])  # Bumrah — last element
print(players[-1])  # Bumrah — negative index (from end)
print(players[-3])  # Jadeja

# Index reference:
# Forward:   0=Dhoni  1=Kohli  2=Jadeja  3=Rohit  4=Bumrah
# Backward: -5=Dhoni -4=Kohli -3=Jadeja -2=Rohit -1=Bumrah

# --- SLICING ---
# Syntax: list[start : end : step]
# Rule: start is INCLUSIVE, end is EXCLUSIVE

print(players[1:3])  # ['Kohli', 'Jadeja'] — index 1 and 2, NOT 3
print(players[:3])  # ['Dhoni', 'Kohli', 'Jadeja'] — first 3
print(players[2:])  # ['Jadeja', 'Rohit', 'Bumrah'] — index 2 to end
print(players[-2:])  # ['Rohit', 'Bumrah'] — last 2 elements
print(players[::2])  # ['Dhoni', 'Jadeja', 'Bumrah'] — every 2nd element
print(players[::-1])  # ['Bumrah', 'Rohit', 'Jadeja', 'Kohli', 'Dhoni'] — reversed

# Step rules:
# Positive step → moves forward
# Negative step → moves backward
# Number = how many positions to jump

# --- LIST OPERATIONS ---
players = ["Dhoni", "Kohli", "Jadeja", "Rohit", "Bumrah"]

players.append("Hardik")  # add to end
print(players)

players.insert(1, "Virat")  # insert at index 1
print(players)

players.remove("Rohit")  # remove by value
print(players)

players.pop(0)  # remove by index
print(players)

players[0] = "Gill"  # modify by index
print(players)

# append = push (stack)
# pop()  = pop last element (stack)
# pop(0) = remove first element

# --- LOOPS ---
players = ["Dhoni", "Kohli", "Jadeja", "Rohit", "Bumrah"]

# Simple loop — values only
for player in players:
    print(player)

# Enumerate — index and value together
for index, player in enumerate(players):
    print(index, player)

# Human-readable numbering (index + 1)
for index, player in enumerate(players):
    print(f"Player {index + 1}: {player}")

# ============================================================
# SECTION 2 — LIST COMPREHENSION
# ============================================================

players = ["Dhoni", "Kohli", "Jadeja", "Rohit", "Bumrah"]

# Syntax: [expression for item in list]
# Syntax: [expression for item in list if condition]
# Syntax: [expression for item in list if condition] — transform + filter

# Transform only
upper_players = [player.upper() for player in players]
print(upper_players)

# Filter only
long_names = [player for player in players if len(player) > 5]
print(long_names)

# Transform and filter together
upper_long = [player.upper() for player in players if len(player) > 5]
print(upper_long)

# String methods used:
# .upper()      → ALL CAPS
# .lower()      → all lowercase
# .capitalize() → First letter capital only (e.g. "virat kohli" → "Virat kohli")
# .title()      → Every Word Capitalized (e.g. "virat kohli" → "Virat Kohli")

# ============================================================
# SECTION 3 — EXERCISES (solved)
# ============================================================

# Exercise 1 — filter scores above 70
scores = [45, 78, 92, 23, 67, 88, 54, 91]
marks = [score for score in scores if score > 70]
print(marks)  # [78, 92, 88, 91]

# Exercise 2 — capitalize names
names = ["dhoni", "kohli", "jadeja", "rohit", "bumrah"]
upper_names = [name.capitalize() for name in names]
print(upper_names)  # ['Dhoni', 'Kohli', 'Jadeja', 'Rohit', 'Bumrah']

# Exercise 3 — square of even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [number ** 2 for number in numbers if number % 2 == 0]
print(result)  # [4, 16, 36, 64, 100]

# Exercise 4 — Celsius to Fahrenheit
temperatures = [23, 35, 18, 42, 29, 15, 38, 27]
degree = [(celsius * 9 / 5) + 32 for celsius in temperatures]
print(degree)  # [73.4, 95.0, 64.4, 107.6, 84.2, 59.0, 100.4, 80.6]

# Exercise 5 — words longer than 4 letters in uppercase
words = ["apple", "banana", "kiwi", "mango", "strawberry", "fig"]
upper_words = [word.upper() for word in words if len(word) > 4]
print(upper_words)  # ['APPLE', 'BANANA', 'MANGO', 'STRAWBERRY']

# Exercise 6 — odd numbers with f-string
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_number = [f"{n} is odd" for n in numbers if n % 2 != 0]
print(odd_number)  # ['1 is odd', '3 is odd', '5 is odd', '7 is odd', '9 is odd']