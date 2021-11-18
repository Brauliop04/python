#Number guessing game
#Braulio Pacheco Romo
#Sep 21, 2021

import random

secret = random.randint(0,99) + 1
 
count = 1
tries = 4
loser = True

for i in range (tries):

  guess = int(input("What is your number? "))

  print("you guessed: ")
  print(guess)

  if guess > secret:
    print("your number is too high")
  elif guess < secret:
    print("Your number is too low")
  elif guess == secret:
    print("You got it!")
    loser = False

    count = count + 1

if loser:
  print("you ran out of tries!")

print("GAME OVER!")      
