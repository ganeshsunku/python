# def reverse_string_loop(s: str) -> str:
#     reversed_str = ""
#     for char in s:
#         # Prepend each character to the accumulated string
#         reversed_str = char + reversed_str
#         print(f"Current character: {char}, Reversed string so far: {reversed_str}")
#     return reversed_str

# # Example usage:
# text = "python"
# print(reverse_string_loop(text))  # Output: nohtyp

# numbers = [1, 2, 3, 2, 4, 3, 5]

# duplicates = list({
#     x for x in numbers
#     if numbers.count(x) > 1
# })

# print(duplicates)  # Output: [2, 3]
# result = []
# for number in numbers:
#     if numbers.count(number) > 1:
#         result.append(number)
# result = list(set(result))  # Remove duplicates from the result list
# print(result)  # Output: [2, 3]


# from collections import Counter

# text = "programming"

# result = Counter(text)

# print(result)



# from collections import Counter

# sentence = "python sql python fastapi sql python"

# result = Counter(sentence.split())

# print(result)

# def my_decorator(func):
#     def wrapper():
#         print("--> Something is happening BEFORE the function is called.")
#         func()        
#         print("--> Something is happening AFTER the function is called.")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello, Ganesh!")

# say_hello()


# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/users")
# def get_users():
#     return {"message": "Users retrieved successfully"}

final_list=[]
for num in range(1,10001):
  sqr_numm = num**2
  length = len(str(sqr_numm))/2
  split_num = str(sqr_numm//10**length).split(".")
#   print(split_num)
  num1 = int(split_num[0])
  num2 = int(split_num[1])
  if num1+num2 == num:
    final_list.append(num)

print(final_list)
  