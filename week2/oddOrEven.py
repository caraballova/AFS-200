
print("Welcome to the game of Odd & Even" " \U0001f600")
num = int(input("Enter a number: "))                                        # Ask the user for a number
if (num % 4) == 0:                                                          # If the number is a multiple of 4
    print(num, "is a multiple of four and an even number.")
elif (num % 2) == 0:                                                        # If the number is even or odd
   print(num, "is an even number.")
else:
   print(num, "is an ODD number.")


num1 = int(input('Please enter your first number : '))                      # Ask the user for
check = int(input('Please enter your second number : '))                   # two numbers

def checkIfEven (number1, number2):
  if number1%number2 == 0:                                                  # if num1 can/cannot be divided by check
    print(str(number1) + ' can be divided by ' + str(number2))
  else:
    print(str(number1) + ' cannot be divided by ' + str(number2))

checkIfEven(num1, check)