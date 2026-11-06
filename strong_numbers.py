# Strong Numbers

# Find numbers equal to the sum of the factorials of their digits.

# Example: 145 → 1! + 4! + 5! = 145.

def is_strong_number(num):
    result = 0
    for i in str(num):
        fact = 1
        for j in range(1, int(i)+1):
            fact *= j
        result += fact
    return result == num

print([num for num in range(1, 10001) if is_strong_number(num)])
