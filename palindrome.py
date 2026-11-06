# Palindrome Numbers

# Find all palindrome numbers between 1 and 10,000 without converting them into strings.

def is_palindrome(num):
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10

    return reversed_num == num

print([num for num in range(1, 10001) if is_palindrome(num)])