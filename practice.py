# Create a function that accepts two numbers and an operation.
def calcualtor(num1, num2, operation):
    if operation=="add":
        return num1+num2
    elif operation=="multiply":
        return num1*num2
    elif operation=="substract":
        if num1>num2:
            return num1-num2
        else:
            return num2-num1

print(calcualtor(10,20, "add"), calcualtor(10,2, "multiply"), calcualtor(20,10, "substract"))


