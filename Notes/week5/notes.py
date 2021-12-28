# Functions

def func1():
   print ("I am learning Python function")
   print ("still in func1")
   
func1()                     # calling the function

def square(x):
  	return x*x
print(square(4))

def multiply(x,y=0):
	print("value of x =",x)
	print("value of y =",y)
    
	return x*y
  
print(multiply(y=2,x=4))

# Lambdas 

adder = lambda x, y: x + y
print(adder(1,2))          # Output - 3


x="some kind of a useless lambda"
(lambda x : print(x))(x)
