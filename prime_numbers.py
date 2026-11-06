# Prime Number Pairs

# Find all pairs of consecutive prime numbers whose difference is 2.

# Example: (3, 5), (5, 7), (11, 13).

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        print(num, int(num**0.5))
        if num % i == 0:
            return False
    return True

prime_pairs = [(i, i + 2) for i in range(2, 100) if is_prime(i) and is_prime(i + 2)]
print(prime_pairs)