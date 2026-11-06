# Find numbers whose square ends with the original number.
# Example: 25 → 25² = 625.

def is_automorphic(num):
    sqr_num = num*num
    if num == sqr_num % (10 ** len(str(num))):
        return True
    return False

print([num for num in range(1, 10001) if is_automorphic(num)])