# Happy Numbers

# Find happy numbers between 1 and 1,000.

# Example: 19 → 1² + 9² = 82 → 8² + 2² = 68 → ... → 1.

def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        sum_of_squares = sum(int(digit)**2 for digit in str(num))
        if sum_of_squares == 1:
            return True
        num = sum_of_squares
    return False

print([num for num in range(1, 1001) if is_happy(num)])