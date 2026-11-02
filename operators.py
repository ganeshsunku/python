# Operators perform operations on variables and values.
# Addition, Subtraction, Multiplication, Division, Floor division, Modulus, Power


# Difference between / and //?
print(10 / 3)   # 3.333333...
print(10 // 3)  # 3
print(-10 // 3)  # -4


# Comparison operators
# These operators return Boolean values.
a = 10
b = 20

print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True

# Difference between = and ==?
# - = assigns a value.
# - == compares two values.

# Logical operators
# Three important logical operators:
# Operator -> and, or, not
age = 25
salary = 50000

print(age > 18 and salary > 30000)  # True
print(age > 30 or salary > 30000)   # True
print(not age > 18)                 # False

# Membership operators
# Used to check whether an element exists inside a sequence or collection.
platforms = ["Okta", "Defender", "Sentinel"]

print("Okta" in platforms)       # True
print("AWS" not in platforms)    # True

message = "Python Security Automation"

print("Python" in message)  # True
print("Java" in message)    # False
# With dictionaries, membership checks keys by default:
user = {
    "name": "Ganesh",
    "role": "Engineer"
}

print("name" in user)  # True
print("Ganesh" in user)  # False

# Identity operators: is and is not
# This is a frequently asked Python interview topic.
# - == compares values.
# - is compares object identity.
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True
print(a is b)  # False
print(a is c)  # True