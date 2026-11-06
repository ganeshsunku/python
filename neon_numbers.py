# Neon Numbers

# Find numbers where the sum of the digits of their square equals the original number.

# Example: 9 → 9² = 81 → 8 + 1 = 9.

def is_neon(num):
    sqr_num = num*num
    digits_sum = sum(int(digit) for digit in str(sqr_num))
    return digits_sum == num

print([num for num in range(1, 10001) if is_neon(num)])