# What is a dictionary?
# A dictionary stores data in key-value pairs.
employee = {
    "name": "Ganesh",
    "age": 28,
    "role": "Python Developer",
    "experience": 4
}

print(employee)

# Accessing dictionary values
# You can access values using their keys.
employee = {
    "name": "Ganesh",
    "age": 28,
    "role": "Python Developer"
}

print(employee["name"])
print(employee["age"])
print(employee["salary"]) # key error

# Dictionary get() method
# get() retrieves a value without raising an error when the key is missing.
employee = {
    "name": "Ganesh",
    "age": 28
}

print(employee.get("name"))
print(employee.get("salary"))
print(employee.get("salary", 0))

# keys()
# Returns all dictionary keys.
user = {
    "name": "Ganesh",
    "role": "Developer",
    "location": "India"
}

print(user.keys())
# values()
# Returns all dictionary values.
print(user.values())

# items()
# Returns key-value pairs as tuples.
print(user.items())

# update()
# Adds new key-value pairs or updates existing values.
user = {
    "name": "Ganesh",
    "role": "Developer"
}

user.update({
    "role": "Senior Developer",
    "age": 28
})

print(user)
# pop()
# Removes a key and returns its value.
user = {
    "name": "Ganesh",
    "role": "Developer",
    "age": 28
}

removed_value = user.pop("age")

print(removed_value)
print(user)

# Dictionary comprehension
# Dictionary comprehension provides a short way to create dictionaries.
# {key_expression: value_expression for item in iterable}
numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)

# What is a set?
# A set is an unordered collection of unique elements.
numbers = {10, 20, 30, 20, 10}

print(numbers)

# remove()
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)