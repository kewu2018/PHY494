# guessinggame.py
import random
number = random.randint(1,1000)
guess  = int(input("Guess the number:"))
n_guesses = 1


while guess != number:
  if guess > number:
    print("the guessing number is too large, guess again")
    guess  = int(input("Guess the number:"))
  elif guess <number:
    print("the guessing number is too small, guess agian")
    guess  = int(input("Guess the number:"))
    n_guesses +=1

print("your guessing is correct")

