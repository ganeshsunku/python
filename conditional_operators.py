# Conditional Statements
# Conditional statements execute code based on whether a condition is true or false.
# if statement
age = 25

if age >= 18:
    print("Eligible to vote")

# If the condition is true, the code inside the if block executes.

# if-else statement
number = 10

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if-elif-else statement
# Used when multiple conditions need to be checked.
status_code = 429

if status_code == 200:
    print("Success")
elif status_code == 401:
    print("Unauthorized")
elif status_code == 429:
    print("Rate limit exceeded")
elif status_code == 503:
    print("Service unavailable")
else:
    print("Unknown response")


# Nested if statements
# An if statement inside another if statement.

username = "admin"
password = "admin123"

if username == "admin":
    if password == "admin123":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")


users = []

if users:
    print("Users available")
else:
    print("No users available")