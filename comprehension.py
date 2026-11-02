# list coprehension
numbers= [1,2,3,4,5]

data = [number**2 for number in numbers]
print(data)

squares = [number**2 for number in numbers if number %2==0]
print(squares)

types=["even" if number %2==0 else "odd" for number in numbers]
print(types)

# dictionary comprehension

dict_squares={number:number**2 for number in numbers}
print(dict_squares)

scores = {
    "Ganesh": 85,
    "Ravi": 45,
    "Kiran": 90,
    "Arun": 35
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 50
}

print(passed)

# Set comprehension
# Set comprehension creates a set containing unique values.