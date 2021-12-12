# Lists are basically an ordered way of grouping things (called elements) - the cool thing about lists in Python is that you can have a list that contains objects of multiple types. 
# Your list can mix between strings, integers, objects, other lists, what have you.
# The way to construct an empty list is to just do

x = []

# And your variable x now holds an empty list. To add things to this list, just “append” them to the list. Like so:

x = []

x.append(3)

# Your list x now looks like [3].

# In Python, lists are also iterables, which means you can loop through them with a for loop in a convenient way. (If you come from other languages like C++ or Java you are most likely used to using a counter to loop through indices of a list - in Python you can actually loop through the elements.) I will let the code speak for itself:

my_list = [1, 3, "Michele", [5, 6, 7]]

for element in my_list:

  print(element)

# Will yield the result:

1

3

"Michele"

[5, 6, 7]

# There are many other properties of lists, but for the basic exercise all you should need is this for loop property. Future weeks will address other properties of lists.

# The nice thing about conditionals is that they follow logical operations. They can also be used to test equality. Let’s do a small example. Let’s say I want to make a piece of code that converts from a numerical grade (1-100) to a letter grade (A, B, C, D, F). The code would look like this:

grade = input("Enter your grade: ")

if grade >= '90':

  print("A")

elif grade >= '80':

  print("B")

elif grade >= '70':

  print("C")

elif grade >= '65':

  print("D")

else:

  print("F")

# What happens if grade is 50? All the conditions are false, so "F" gets printed on the screen. But what if grade is 95? Then all the conditions are true and everything gets printed, right?  
# Nope! What happens is the program goes line by line. The first condition (grade >= 90) is satisfied, so the program enters into the code inside the ifstatement, executing print("A"). 
# Once code inside a conditional has been executed, the rest of the conditions are skipped and none of the other conditionals are checked.

# If and then else statements
# Example file for working with conditional statement

def main():
	x,y =8,4
	
	if(x < y):
		st= "x is less than y"
	else:
		st= "x is greater than y"
	print (st)
	
if __name__ == "__main__":
	main()



def SwitchExample(argument):
    switcher = {
        0: " This is Case Zero ",
        1: " This is Case One ",
        2: " This is Case Two ",
    }
    return switcher.get(argument, "nothing")


if __name__ == "__main__":
    argument = 1
    print (SwitchExample(argument))

# Lists in Python
# a container that contains different python objects

friends = ['Jeremiah', 'Michael', 'Vanessa', 'Christian']
print(friends)

print(friends[2])     # Output: Vanessa
print(len(friends))   # Output: 4
print(friends.count('Vanessa')) # Output 1
friends.sort()
print(friends)        # Output ['Christian', 'Jeremiah', 'Michael', 'Vanessa']
friends.reverse()
print(friends)

cars = [911, 130, 582, 897, 732, 914] 
print(cars)
print(min(cars))      # Output 130 Prints lowest number on list

friends[2] = 'Bob'
friends.extend(cars)  # add cars to the list
print(friends)        # Output ['Christian', 'Bob', 'Michael', 'Vanessa', 911, 130, 582, 897, 732, 914]
print(sum(cars))      # Output 4166

friends.remove('Bob') # remove Bob from the list
print(friends)        # Output ['Christian', 'Michael', 'Vanessa', 911, 130, 582, 897, 732, 914]

del friends[2]
print(friends)

new_friends=friends.copy() # creates a copy of the list
print(friends)


# Splits & Joins

msg = 'Welcome to Python Django Course: Split and Join'
csv = 'Jeremiah, Christian, Michael, Vanessa'
friends_list = ['Jeremiah', 'Christian', 'Michael', 'Vanessa']
print(msg.split())
print('-'.join(friends_list))
print('-'.join(friends_list + friends_list))
print(' '.join(friends_list))

# Tuples & Python

tup1 = ('Robert', 'Carlos','1965','Terminator 1995', 'Actor','Florida');
tup2 = (1,2,3,4,5,6,7);
print(tup1[0])    # Will print 'Robert'
print(tup2[1:4])  # Will print 2 through 4


x = ("Guru99", 20, "Education")    # tuple packing
(company, emp, profile) = x    # tuple unpacking
print(company)
print(emp)
print(profile)


a = (5,6)
b = (1,4)
if (a>b):
  print("A is bigger")
else: 
  print("B is bigger")

# Slicing Tuples

x = ("a", "b","c", "d", "e")
print(x[2:4]) # Output ('c','d')

# Tuples in Dictionary

a = {'x':100, 'y':200}
b = list(a.items())
print(b)                  # Output [('x', 100), ('y', 200)]