import random

# Get name of user
name = input("Hello, what is your name? ")

# Greet user
print(f"Hello {name}! Welcome to the Number Guessing Game. You have 7 attempts to guess the number. Let's start!")

# Accept lower bound
lower = int(input("Enter a lower bound: "))

# Accept upper bound
upper = int(input("Enter an upper bound: "))

# Generate random number
num = random.randint(lower, upper)

# Chances for user
chances = 7

# Keep track of guesses
guess_counter =  0 

# Loop as long as guesses less than chances
while guess_counter < chances:

    # Increment guess counter each time
    guess_counter += 1
    
    # Get guess
    guess = int(input("Enter you guess: "))

    # See if guess is correct or not
    if guess == num:
        print(f"Correct! The number is {guess}!")
        break
    elif guess_counter >= chances and guess != num:
        print(f"Sorry {name}! The number was {num}. Better luck next time.")
        break
    elif guess > num:
        print("Too high! Try a lower number.")
    else:
        print("Too low! Try a higher number.")

    # Print chances left
    print(f"You have {chances - guess_counter} chances left.")
