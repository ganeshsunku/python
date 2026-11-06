def is_prime(n):
    if n < 2:
        return False

    divisor = 2

    while divisor * divisor <= n:
        print(divisor*divisor)
        if n % divisor == 0:
            return False
        divisor += 1

    return True


print(is_prime(7))   # True
print(is_prime(12))  # False
print(is_prime(1))   # False


def factorial(n):
    if n < 0:
        raise ValueError("Factorial requires a non-negative integer.")

    result = 1

    for number in range(1, n + 1):
        result *= number

    return result


print(factorial(5))  # 120
print(factorial(0))  # 1

def fibonacci(n):
    if n < 0:
        raise ValueError("The number of terms cannot be negative.")

    series = []
    a, b = 0, 1

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series


print(fibonacci(7))  # [0, 1, 1, 2, 3, 5, 8]
print(fibonacci(0))  # []


def count_vowels_consonants(text):
    vowels = 0
    consonants = 0

    for char in text.lower():
        if "a" <= char <= "z":
            if char in "aeiou":
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


vowels, consonants = count_vowels_consonants("Hello World!")

print("Vowels:", vowels)          # Vowels: 3
print("Consonants:", consonants)  # Consonants: 7

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


print(largest_of_three(10, 25, 15))  # 25
print(largest_of_three(8, 8, 3))     # 8


def sum_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        total += number % 10
        number //= 10

    return total


print(sum_digits(12345))  # 15
print(sum_digits(-456))   # 15
print(sum_digits(0))      # 0

def separate_even_odd(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers


values = [1, 2, 3, 4, 5, 6, 0, -3, -4]
evens, odds = separate_even_odd(values)

print("Even:", evens)  # Even: [2, 4, 6, 0, -4]
print("Odd:", odds)    # Odd: [1, 3, 5, -3]


def sum_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        total += number % 10
        print(" number ------>",number%10)
        number //= 10

    return total


print(sum_digits(12345))  # 15
print(sum_digits(-456))   # 15
print(sum_digits(0))      # 0

def second_largest(numbers):
    unique = sorted(set(numbers))

    if len(unique) < 2:
        return None

    return unique[-2]


print(second_largest([10, 5, 20, 20, 8]))  # 10
print(second_largest([7, 7]))              # None





















