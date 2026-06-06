# ============================================================
# SECTION 1 — WHAT IS A DICTIONARY?
# ============================================================

# A dictionary stores data as key-value pairs
# Access data by meaningful key, not by index like a list

# Syntax:
# dict = {"key": value, "key": value}

# JS equivalent — Objects
# Python dict    → JS Object
# dict["key"]    → obj["key"] or obj.key
# dict.keys()    → Object.keys(obj)
# dict.values()  → Object.values(obj)
# dict.items()   → Object.entries(obj)


# ============================================================
# SECTION 2 — CREATING AND ACCESSING
# ============================================================

player = {
    "name": "Dhoni",
    "age": 42,
    "role": "Wicket Keeper",
    "is_captain": True
}

print(player)  # full dictionary
print(type(player))  # <class 'dict'>
print(player["name"])  # Dhoni
print(player["age"])  # 42

# ============================================================
# SECTION 3 — DICTIONARY METHODS
# ============================================================

print(player.keys())  # dict_keys(['name', 'age', 'role', 'is_captain'])
print(player.values())  # dict_values(['Dhoni', 42, 'Wicket Keeper', True])
print(player.items())  # dict_items([('name', 'Dhoni'), ('age', 42)...])

# Check if key exists
print("name" in player)  # True
print("height" in player)  # False

# ============================================================
# SECTION 4 — LOOPING THROUGH A DICTIONARY
# ============================================================

# Loop through key-value pairs using .items()
for key, value in player.items():
    print(f"{key}: {value}")

# Output:
# name: Dhoni
# age: 42
# role: Wicket Keeper
# is_captain: True


# ============================================================
# SECTION 5 — DICTIONARY OPERATIONS
# ============================================================

player = {
    "name": "Dhoni",
    "age": 42,
    "role": "Wicket Keeper",
    "is_captain": True
}

# Adding a new key
player["jersey_number"] = 7
print(player)

# Updating existing key
player["age"] = 43
print(player)

# Removing a key — no return value
del player["is_captain"]
print(player)

# Safe removal — returns the removed value
role = player.pop("role")
print(role)  # Wicket Keeper
print(player)  # {'name': 'Dhoni', 'age': 43, 'jersey_number': 7}

# del vs pop:
# del dict["key"]       → removes, returns nothing
# dict.pop("key")       → removes, returns the value


# ============================================================
# SECTION 6 — NESTED DICTIONARIES
# ============================================================

# A dictionary inside another dictionary
# Same as nested objects in JS

team = {
    "Dhoni": {
        "age": 42,
        "role": "Wicket Keeper",
        "jersey": 7
    },
    "Kohli": {
        "age": 35,
        "role": "Batsman",
        "jersey": 18
    },
    "Jadeja": {
        "age": 35,
        "role": "All Rounder",
        "jersey": 8
    }
}

# Accessing nested values
# Syntax: dict["outer_key"]["inner_key"]
# JS equivalent: obj.outerKey.innerKey

print(team["Kohli"]["jersey"])  # 18
print(team["Dhoni"]["role"])  # Wicket Keeper
print(team["Jadeja"]["age"])  # 35

# Go as deep as needed:
# response["user"]["profile"]["name"]  → three levels deep


# ============================================================
# SECTION 7 — LOOPING NESTED DICTIONARIES
# ============================================================

for player, details in team.items():
    print(f"{player} - Role: {details['role']}, Jersey: {details['jersey']}")

# Output:
# Dhoni - Role: Wicket Keeper, Jersey: 7
# Kohli - Role: Batsman, Jersey: 18
# Jadeja - Role: All Rounder, Jersey: 8

# Note: use single quotes inside f-string when f-string uses double quotes
# f"{details['role']}"  ← correct
# f"{details["role"]}"  ← quote conflict — wrong


# ============================================================
# SECTION 8 — REAL WORLD DE EXAMPLE
# ============================================================

# APIs return nested JSON — Python dictionaries handle this naturally
response = {
    "user": {
        "id": 123,
        "profile": {
            "name": "Kirthivasan",
            "role": "Data Engineer"
        }
    }
}

print(response["user"]["profile"]["name"])  # Kirthivasan
print(response["user"]["id"])  # 123

# ============================================================
# SECTION 9 — EXERCISE (solved)
# ============================================================

# Exercise — loop through team and print player details
team = {
    "Dhoni": {"age": 42, "role": "Wicket Keeper", "jersey": 7},
    "Kohli": {"age": 35, "role": "Batsman", "jersey": 18},
    "Jadeja": {"age": 35, "role": "All Rounder", "jersey": 8}
}

for player, details in team.items():
    print(f"{player} - Role: {details['role']}, Jersey: {details['jersey']}")