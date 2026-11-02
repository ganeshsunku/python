# Check whether a number is even or odd
def check_even_odd(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"

# Example
print(check_even_odd(42))  # Even
print(check_even_odd(7))   # Odd


# Find the largest of three numbers
def largest_of_three(a: float, b: float, c: float) -> float:
    # Conditional logic approach
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    return c

# Example
print(largest_of_three(12.5, 45.2, 33.1))  # 45.2

# 3. Check whether a number is positive, negative, or zero
def classify_number(n: float) -> str:
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

# Example
print(classify_number(-8.5))  # Negative

# 4. Print numbers from 1 to 100
def print_1_to_100() -> None:
    for i in range(1, 101):
        print(i, end=" ")
    print()

# Example run: 1 2 3 ... 100
# 5. Print even numbers between 1 and 50
def print_evens_1_to_50() -> None:
    # Starts at 2, increments by 2 up to 50 inclusive
    for i in range(2, 51, 2):
        print(i, end=" ")
    print()

# Example run: 2 4 6 ... 50

# 6. Find the sum of numbers from 1 to N
def sum_1_to_n_loop(n: int) -> int:
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_1_to_n_formula(n: int) -> int:
    return n * (n + 1) // 2

# Example
print(sum_1_to_n_loop(10))     # 55
print(sum_1_to_n_formula(10))  # 55

# 7. Calculate factorial of a number
def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example
print(calculate_factorial(5))  # 120

# 8. Reverse a string using a loop
def reverse_string_loop(s: str) -> str:
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example
print(reverse_string_loop("python"))  # nohtyp

# 9. Check whether a string is a palindrome
def is_palindrome(text: str) -> bool:
    # 1. Normalize: lowercase and remove non-alphanumeric characters
    cleaned = "".join(char.lower() for char in text if char.isalnum())
    
    # 2. Compare string to its reverse
    return cleaned == cleaned[::-1]


# Tests
print(is_palindrome("racecar"))                         # True
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("hello"))                           # False

# 10. Count vowels in a string
def count_vowels(s: str) -> int:
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example
print(count_vowels("Hello World"))  # 3

# 11. Find duplicate numbers in a list
def find_duplicates(nums: list[int]) -> list[int]:
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example
print(find_duplicates([1, 2, 3, 2, 4, 5, 1, 6]))  # [1, 2]

# 12. Combine two lists using zip()
def combine_lists(keys: list, values: list) -> list[tuple]:
    combined = []
    for key, value in zip(keys, values):
        combined.append((key, value))
    return combined

# Example
students = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]
print(combine_lists(students, scores))
# [('Alice', 92), ('Bob', 85), ('Charlie', 78)]

def combine_lists(keys: list, values: list) -> list[tuple]:
    combined = []
    for i in range(min(len(keys),len(values))):
        combined.append((keys[i], values[i]))
    return combined
# Example
students = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]
print(combine_lists(students, scores))

# 13. Print index and value using enumerate()
def display_indexed_items(items: list) -> None:
    for index, value in enumerate(items, start=0):
        print(f"Index {index} -> {value}")

# Example
display_indexed_items(["Python", "Rust", "Go"])
# Index 0 -> Python
# Index 1 -> Rust
# Index 2 -> Go

# Implement an API retry mechanism with 3 attempts

def service_unavailabe():
    raise Exception

def retry_mechanism(max_retries: int):
    for retry in range(1, max_retries+1):
        try:
            service_unavailabe()
        except Exception as exp:
            print(f"exception occusr for the retry {retry} for exp {exp}")
            retry+=1
    raise RuntimeError(f"API request failed after {max_retries} attempts.")

try:
    data = retry_mechanism(3)
    print(data)
except Exception:
    print(Exception)
# 15. Process a list of users and skip blocked accounts
def process_active_users(users: list[dict]) -> list[str]:
    processed_emails = []
    for user in users:
        # Skip user if marked as blocked
        if user.get("is_blocked", False):
            continue
        
        # Process active user
        processed_emails.append(user["email"])
    return processed_emails

# Example
user_data = [
    {"id": 1, "email": "alice@example.com", "is_blocked": False},
    {"id": 2, "email": "spammer@example.com", "is_blocked": True},
    {"id": 3, "email": "carol@example.com", "is_blocked": False},
]

print(process_active_users(user_data))
# ['alice@example.com', 'carol@example.com']
