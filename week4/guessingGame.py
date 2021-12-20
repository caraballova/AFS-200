import random

guesses = 0
randomNumber = random.randint(1,10)
name = input("What is your name? ")
print('Welcome ' + name + "! Let's have some fun and play a guessing game!" + "\U0001f600")
print('I am thinking of a number ' + '\U0001F914')

while randomNumber != "guess":
    guess = int(input('Enter a number between 1 and 9: '))
    if guess == randomNumber:
        print('Yay, you guessed it! ' + "\U0001F973")
        guesses += 1
        print('Number of guesses', guesses)
        break        
    if guess < randomNumber:
        guesses += 1
        print('Too low, Try again ' + '\U0001F641')     
    if guess > randomNumber:
        guesses += 1
        print('Too high, try again ' + '\U0001F641')
            
    
        
    



