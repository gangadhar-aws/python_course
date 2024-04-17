
def add(n1, n2):
    return n1+n2

def subtract(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def calculator(a, b, func):
    return func(a, b)

result = calculator(10, 5, multiply)
print(result)
