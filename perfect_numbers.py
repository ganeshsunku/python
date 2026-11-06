# Find all perfect numbers from 1 to 10,000.

def is_perfect(num):
    if num < 2:
        return False
    divisors_sum = 0
    for i in range(1, num):
        if num%i == 0:
            divisors_sum += i
    return divisors_sum == num
print([num for num in range(1, 10001) if is_perfect(num)])
