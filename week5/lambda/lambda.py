def multiply(a):
    return lambda x : x * a

x = multiply(89)
print(x(5))