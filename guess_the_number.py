import random
"""
Write a program that generates a random number and prompts the user to guess the number.
"""
"""
Create a new file called guess_the_number.py. 
In the file, use the random module to generate a random number between 1 and 100. 
Prompt the user to guess the number and provide feedback (higher or lower) 
until the user guesses the correct number. 
Print the number of guesses it took the user to guess the number.
"""


n = random.randrange(1, 5)
guess = int(input("Enter any number: "))
guess_number = 1
while n != guess:
    guess_number = guess_number + 1
    if guess < n:
        print("Your guess is too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Your guess is too high!")
        guess = int(input("Enter number again: "))
    else:
        break
print("Your guess is correct!!")
print("You guessed", guess_number, "times to get the correct number!")
