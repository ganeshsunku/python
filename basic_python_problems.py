# Reverse a string without using [::-1]
def reverse_string(input_str):
    final_str="".join(input_str)
    return input_str==final_str[::-1]
print(reverse_string("vav"))

# Check whether a number is even or odd.
def is_even_or_odd(num):
    if num%2==0:
        print("even")
    elif num%2!=0:
        print("odd")
is_even_or_odd(33)

# Find the largest of three numbers.

def is_largest(a,b,c):
    if a>=b and a>=c:
        print(a)
    elif b>=a and b>=c:
        print(b)
    else:
        print(c)
is_largest(2423,547,979)

# Check whether a number is prime.
def is_prime(num):
    if num<1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
print([i for i in range(2,100) if is_prime(i)]) 

# Find the factorial of a number.

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact = fact*i
    return fact
print([factorial(i) for i in range(1,100)])

# Generate the Fibonacci series.
def fibanacci(num):
    if num<0:
        return []
    elif num == 1:
        return [0]
    series=[0,1]
    while len(series)<num:
        series.append(series[-1]+series[-2])
    return series
print(fibanacci(5))

# Check whether a number is a palindrome.
def palindrome(num):
    reverse_num=""
    for i in str(num):
        reverse_num=i + reverse_num 
    return num == int(reverse_num)

print([num for num in range(1,1000) if palindrome(num)])

# Check whether a number is an Armstrong number.
# • Single Digits: Every single-digit number (1–9) is an Armstrong number because x¹ = x.
# • 3-Digit Example (153): It has 3 digits, so we cube each digit:
# 1^{3}+5^{3}+3^{3}=1+125+27=\mathbf{153}
def is_armstrong(num):
    sum=0
    for i in str(num):
        sum+=int(i)**(len(str(num)))
    return num == sum
print([num for num in range(1, 1000) if is_armstrong(num)])


# Find the sum of digits of a number.
def sum_digit(num):
    sum=0
    for i in str(num):
        sum+=int(i)
    return sum
print([sum_digit(num) for num in range(1,10)])

# Count the number of digits in an integer.
def count_int(num):
    return len(str(num))
print([count_int(num) for num in range(1,100)])

# Reverse an integer.
def reverse_int(num):
    reverse=""
    for i in str(num):
        reverse=i+reverse
    return reverse
print([reverse_int(num) for num in range(1, 100)])
# Find the largest element in a list.

def largest_numin_list(input_list):
    largest_num = 0
    for i in input_list:
        if i>largest_num:
            largest_num=i
    return largest_num
print(largest_numin_list([123,34536,5675,2354236,8585]))

# Find the second-largest element without sorting.
def second_largest__list(input_list):
    fisrt_larget=0
    second_largest=0
    for i in input_list:
        if i>fisrt_larget:
            second_largest=fisrt_larget
            fisrt_larget=i
        elif i>second_largest and i!=fisrt_larget:
            second_largest=i
    return second_largest
print(second_largest__list([12314,3453464,568756842,2,5,7,89,234,657,23]))
# Find the smallest and second-smallest elements.

def smallest_second_smallest(input_list):
    smallest_num = float('inf')
    second_smallest_num = float('inf')
    for i in input_list:
        if i<smallest_num:
            second_smallest_num=smallest_num
            smallest_num=i
        elif i<second_smallest_num and i!=smallest_num:
            second_smallest_num=i
    return smallest_num, second_smallest_num

print(smallest_second_smallest([123,14235,345,6587,12331,3,45,561,5,56,868,1232]))

# Find duplicate elements in a list.

def duplicate_num(input_list):
    seen=[]
    duplicate_nums=[]
    for i in input_list:
        if i in seen:
            duplicate_nums+=[i]
        else:
            seen+=[i]
    return duplicate_nums
print(duplicate_num([1,4,56,7,23,868,23,5,7,56,3,2,12,3,44]))