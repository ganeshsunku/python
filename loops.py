# Loops are used to execute a block of code repeatedly.

# Python mainly provides two types of loops:
# - for loop
# - while loop

# For loop
# Used to iterate over sequences such as lists, tuples, strings, and ranges.

platforms = ["Okta", "Defender", "Sentinel"]

for platform in platforms:
    print(platform)

# range()
# The range() function generates a sequence of integers.
# range(start, stop, step)

# 0 to 4
for i in range(5):
    print(i)

# 1 to 5
for i in range(1, 6):
    print(i)

# Even numbers
for i in range(2, 11, 2):
    print(i)

# Reverse
for i in range(5, 0, -1):
    print(i)


# enumerate()
# enumerate() returns both the index and the value while iterating.
# Without enumerate:
platforms = ["Okta", "Defender", "Sentinel"]

for i in range(len(platforms)):
    print(i, platforms[i])

# With enumerate:
platforms = ["Okta", "Defender", "Sentinel"]

for index, platform in enumerate(platforms):
    print(index, platform)

# zip()
# zip() combines multiple iterables element by element.

users = ["User1", "User2", "User3"]

statuses = ["Active", "Blocked", "Active"]

for user, status in zip(users, statuses):
    print(user, status)

# What happens if the lists have different lengths?
# By default, zip() stops at the shortest iterable.
a = [1, 2, 3, 4]
b = ["A", "B"]

print(list(zip(a, b)))  # [(1, 'A'), (2, 'B')]



# while loop
# A while loop executes as long as the condition remains true.
count = 1

while count <= 5:
    print(count)
    count += 1

attempt = 1
max_retries = 3

while attempt <= max_retries:
    print(f"API attempt: {attempt}")

    # Simulate unsuccessful request
    attempt += 1

print("Maximum retries completed")


# break, continue, and pass
# These are loop control statements.
# break
# Immediately terminates the loop.

for i in range(1, 10):
    if i == 5:
        break

    print(i)

# continue
# Skips the current iteration and moves to the next iteration.

for i in range(1, 6):
    if i == 3:
        continue

    print(i)

# pass
# Does nothing. Used as a placeholder when a statement is syntactically required.

for i in range(1, 6):
    if i == 3:
        pass

    print(i)

# Nested loops
# A loop inside another loop.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)