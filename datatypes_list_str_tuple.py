# Indexing and Slicing
# Indexing is used to access individual elements in a sequence. Slicing is used to extract multiple elements.

# Python supports indexing and slicing for strings, lists, and tuples.
# 1.1 Positive indexing
# Indexing starts from 0.
languages = ["Python", "Java", "Go", "C++"]

print(languages[0])  # Python
print(languages[1])  # Java
print(languages[2])  # Go
print(languages[3])  # C++

# 1.2 Negative indexing
# Negative indexing starts from the last element.
languages = ["Python", "Java", "Go", "C++"]

print(languages[-1])  # C++
print(languages[-2])  # Go
print(languages[-3])  # Java
print(languages[-4])  # Python


# Slicing
# Syntax: sequence[start:stop:step]
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50, 60]
print(numbers[:])     # Full list
print(numbers[::2])   # [10, 30, 50]
print(numbers[1::2])  # [20, 40, 60]

# Reverse slicing – [::-1]
name = "PYTHON"

print(name[::-1])


# Lists in Python
# A list is an ordered, mutable collection that allows duplicate values and elements of different data types.
# 2.1 Creating lists

numbers = [10, 20, 30, 40]

names = ["Ganesh", "John", "David"]

mixed = [10, "Python", 20.5, True]

empty_list = []

print(numbers)
print(names)
print(mixed)

# Mutability
# Lists are mutable. This means we can modify their contents after creation.
numbers = [10, 20, 30]

numbers[1] = 100

print(numbers)
# List methods
# These are particularly important for coding interviews.
# A. append()
# Adds one element to the end of a list.
numbers = [10, 20, 30]

numbers.append(40)

print(numbers)
# extend()
# Adds multiple elements from an iterable.
numbers = [10, 20, 30]

numbers.extend([40, 50])

print(numbers)

# insert()
# Inserts an element at a specific index.
numbers = [10, 20, 40]

numbers.insert(2, 30)

print(numbers)
# D. pop()
# Removes and returns an element.
numbers = [10, 20, 30, 40]

value = numbers.pop()

print(value)    # 40
print(numbers)  # [10, 20, 30]
numbers.pop(1)
print(numbers)

# remove()
# Removes the first matching value.
numbers = [10, 20, 30, 20]

numbers.remove(20)

print(numbers)

# sort()
# Sorts the list in ascending order by default.
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)
# Descending order:
numbers.sort(reverse=True)

print(numbers)

# List comprehension
# A concise way to create lists.
numbers = [1, 2, 3, 4, 5]

squares = [x ** 2 for x in numbers]

print(squares)

# Tuples in Python
# A tuple is an ordered collection that is immutable.
# 
# Unlike lists, tuple elements cannot be changed after creation.
numbers = (10, 20, 30, 40)

names = ("Ganesh", "John", "David")

mixed = (10, "Python", 20.5, True)

print(numbers)
print(names)
print(mixed)
# Immutability
numbers = (10, 20, 30)

numbers[1] = 100  # TypeError
data = (10, [20, 30])

data[1].append(40)

print(data) # (10, [20, 30, 40])

# Single-element tuple
# This is a common interview question.
a = (10)
print(type(a))  # int

# This is not a tuple.

# Correct syntax:
a = (10,)

print(type(a))  # tuple
# Tuple packing
# Combining multiple values into one tuple.
user = "Ganesh", 28, "Python"

print(user)
print(type(user))
# Tuple unpacking
# Extracting tuple elements into individual variables.
user = ("Ganesh", 28, "Python")

name, age, skill = user

print(name)
print(age)
print(skill)
# Tuple methods
# Tuples have two main built-in methods.
numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))  # 3
print(numbers.index(20))  # 1


# String Manipulation in Python
# A string is an immutable sequence of Unicode characters.

# Strings are widely used in backend development, API integrations, log processing, and security automation.
# 4.1 Creating strings
name = "Ganesh"

message = 'Welcome to Python'

description = """Python is a programming language.
It is used for backend development."""
# Strings support indexing and slicing.
language = "PYTHON"

print(language[0])   # P
print(language[-1])  # N
print(language[1:4]) # YTH
print(language[::-1]) # NOHTYP

# String immutability
# Strings cannot be changed directly.
name = "Python"

name[0] = "J"  # TypeError
# Instead, create a new string:
name = "Python"

name = "J" + name[1:]

print(name)  # Jython
# Important string methods
# A. split()
# Splits a string into a list.
message = "Python,Java,Go"

result = message.split(",")

print(result)
# join()
# Joins elements of an iterable into a string.
languages = ["Python", "Java", "Go"]

result = ",".join(languages)

print(result)
# strip()
# Removes leading and trailing whitespace by default.
text = "   Python   "

print(text.strip())   # "Python"
print(text.lstrip())  # "Python   "
print(text.rstrip())  # "   Python"

# replace()
# Replaces matching text.
message = "Hello Java"

result = message.replace("Java", "Python")

print(result)