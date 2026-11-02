# 1. What is a variable in Python?
# Answer: A variable is a name that refers to an object stored in memory.

user_name = "Ganesh"  # Valid
age = 28             # Valid
_salary = 50000       # Valid

# 2age = 28            # Invalid
# user-name = "Test"   # Invalid
# class = "Python"     # Invalid: keyword

print(user_name)
print(age)
print(_salary)

# 2. Is it necessary to declare the variable type in Python?
# Answer: No. Python is dynamically typed. We don't need to declare the data type explicitly. Python determines the type from the assigned object.
x = 10
print(type(x))

x = "Python"
print(type(x))
# How do you check the type of a variable?
# Use the type() function.
a = 100
b = 10.5
c = "Hello"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
# -------------------------------------------------------------------------------------
# What are the primitive data types in Python?
# Data type int, float, str, bool, list, tuple, set, dict, complex, bytes, and NoneType.
# Numeric Types: int, float, complex, bool
# Sequence Types: str, list, tuple, bytes
# Hash-Based Collections: set, dict
# The Singleton: NoneType

# Primitive data types
# int, float, str, bool
a = 100
b = 10.5
c = "Python"
d = True

print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'str'>
print(type(d))  # <class 'bool'>


# Type casting

# String to integer
age = "25"
age = int(age)
print(age + 5)  # 30

# Integer to string
number = 100
number = str(number)
print(number)   # "100"

# String to float
price = "99.50"
price = float(price)
print(price)    # 99.5

# Integer to boolean
print(bool(1))  # True
print(bool(0))  # False

value = "hello"
number = int(value)  # ValueError

# Dynamic typing
# Python determines the type at runtime.
value = 100
print(type(value))

value = "Python"
print(type(value))

value = True
print(type(value))


# What is the difference between int and float?
# int represents whole numbers. converts bool, float, complex data types into int
# float represents floating-point numbers. converts bool, int, complex
a = 10
b = 10.5

print(a + b)
print(type(a + b))

# Is bool an integer in Python?
# Yes. In Python, bool is a subclass of int.
print(True + True)    # 2
print(False + 10)     # 10
print(isinstance(True, int))  # True

#  What is None in Python?
# None represents the absence of a value.
result = None

print(result)
print(type(result))

# What is the difference between static typing and dynamic typing?
# - Static typing: Types are checked or declared before runtime, depending on the language.
# - Dynamic typing: Types are determined at runtime

# Note: Python also supports optional type hints, which help static analysis tools detect type problems.
name: str = "Rahul"
age: int = 25
print(name, age)

# . What is the difference between mutable and immutable objects?
# - Mutable: Can be modified after creation, e.g. list and dictionary.
# - Immutable: Cannot be modified after creation, e.g. integer, float, string, and tuple.