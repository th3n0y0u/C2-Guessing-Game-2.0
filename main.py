import random
# Introduction + rules + options

print("Welcome to a another guessing game where I totally didn't steal this from a project that I needed to do\n")
print("Easy = 1")
print("Medium = 2")
print("Hard = 3") 

userLevel = input("Please choose a difficulty, or enter 'q' if you don't care: ")
tries = 1 

# Game

while(userLevel != 'q'):
  tries = 1
  if(userLevel == '1'):
    computerNumber = random.randint(1,10)
    userInput = int(input("Guess a number between 1 - 10: "))
  if(userLevel == '2'): 
    computerNumber =  random.randint(1,50)
    userInput = int(input("Guess a number between 1 - 50: "))
  if(userLevel == '3'):
    computerNumber = random.randint(1,100)
    userInput = int(input("Guess a number between 1 - 100: "))

  while(userInput != computerNumber):
    if(userInput > computerNumber):
      userInput = int(input("Try again you are too high:"))
      tries += 1
      continue
    elif(userInput < computerNumber):
      userInput = int(input("Try again you are too low: "))
      tries += 1
      continue

  print("You have guessed correctly!")
  print("You have did " + str(tries) + " tries")
  userLevel = input("Do you want to exit, or choose a different difficulty?: ")


print("Thanks for giving a dislike on this game!")