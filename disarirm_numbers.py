# Disarium Numbers

# Find numbers equal to the sum of their digits raised to their respective positions.

# Example: 135 → 1¹ + 3² + 5³ = 135.

def is_disarium(num):
    str_num = str(num)
    sum_of_powers = 0
    for i in str_num:
        sum_of_powers += int(i) ** (str_num.index(i) + 1)
    return sum_of_powers == num

print([num for num in range(1, 1001) if is_disarium(num)])