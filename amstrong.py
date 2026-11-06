# Find all Armstrong numbers from 1 to 10,000.


def is_armstrong(num):
    """Check if a number is an Armstrong number."""
    n = len(str(num))
    total = sum(int(digit) ** n for digit in str(num))
    return total == num

# Find all Armstrong numbers from 1 to 10,000
armstrong_numbers = [num for num in range(1, 10001) if is_armstrong(num)]
print(armstrong_numbers)

