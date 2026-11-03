# # 1. What is a variable in Python?
# # Answer: A variable is a name that refers to an object stored in memory.
# name = "Rahul"
# age = 25
# salary = 35000.50
# is_employee = True

# print(name)
# print(age)
# print(salary)
# print(is_employee)

# # 2. Is it necessary to declare the variable type in Python?
# # Answer: No. Python is dynamically typed. We don't need to declare the data type explicitly. Python determines the type from the assigned object.
# x = 10
# print(type(x))

# x = "Python"
# print(type(x))
# # How do you check the type of a variable?
# # Use the type() function.
# a = 100
# b = 10.5
# c = "Hello"
# d = True

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# # -------------------------------------------------------------------------------------
# # What are the primitive data types in Python?
# # Data type int, float, str, bool, list, tuple, set, dict, complex, bytes, and NoneType.
# # Numeric Types: int, float, complex, bool
# # Sequence Types: str, list, tuple, bytes
# # Hash-Based Collections: set, dict
# # The Singleton: NoneType

# # What is the difference between int and float?
# # int represents whole numbers.
# # float represents floating-point numbers.
# a = 10
# b = 10.5

# print(a + b)
# print(type(a + b))

# # Is bool an integer in Python?
# # Yes. In Python, bool is a subclass of int.
# print(True + True)    # 2
# print(False + 10)     # 10
# print(isinstance(True, int))  # True

# #  What is None in Python?
# # None represents the absence of a value.
# result = None

# print(result)
# print(type(result))

# # What is the difference between dynamic typing and static typing?
# # Dynamic typing
# # Type checked at runtime
# # Variable names can refer to different types
# # Python

# # Static typing
# # Types checked before execution, generally
# # Types are more constrained by the type system
# # Java, C (examples)

# # Note: Python also supports optional type hints, which help static analysis tools detect type problems.
# name: str = "Rahul"
# age: int = 25
# print(name, age)
# # mutable --------------------------------
# print("list")
# a=[1,2,2]
# print(a)
# a[1]=3 # modify 
# a.append(3) # add new
# print(a)
# a.pop(0)
# print(a)
# print("list")
# # ------------------------
# print("dict")
# b={"name":"ganesh", "age":25, "age":40}
# print(b)
# b["age"]=30
# b["place"]="bangalore"
# print(b)

# print("dict")
# # ------------------------------------
# print("tuple")
# b=(1,2,3,4,2)
# print(b)
# print(b.index(3))
# print("tuple")

# #------------------
# print("set")
# c={1,2,3,4,1}
# print(c)

# c.add(5)
# print(c)
# print("set")
a=[1,2,3]
b=a
b[2]=4

print(a,b)

c=[2,345365,6436,7,87121,7,234,9,00,12,45,67,234,768]
print(sorted(c))
c=[2,345365,6436,7,87121,7,234,9,00,12,45,67,234,768]

c.sort()
print(c)
c=[2,345365,6436,7,87121,7,234,9,00,12,45,67,234,768]
c.sort(reverse=True)
print(c)
c=[2,345365,6436,7,87121,7,234,9,00,12,45,67,234,768]
c.reverse()
print(c)

d=1
e=2
# swap
# f=d
# d=e
# e=f
# print(d,e)

if d>e:
    print(d)
elif e>d:
    print(e)

def greet():
    return "Hello Ganesh"

message = greet()

print(message)