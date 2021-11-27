name = input("Enter your name:")

age = int(input("Enter your age:"))

year = int(input("Enter the present year:"))

t=100-age

if t>=100:

   print("You already made it to 100!")

else:

   ans=year+t

   print("Hi " + name + "!" + " You are " + str(age) + " years old" + " and you will turn 100 years old in the year",str(ans) + " \U0001f600")





