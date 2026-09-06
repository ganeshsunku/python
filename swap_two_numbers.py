# how to swap two numbers
a=10
b=5

# senario 1
temp=a
a=b
b=temp
print(a)
print(b)
# --------
# senario 2
a,b=b,a
print(a)
print(b)
# ------------
 # senario 3

a=a+b
b=a-b
a=a-b
print(a)
print(b)
