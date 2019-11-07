"""
My First Python Project
@Author:Raidon Nguyen
@Param:numb, rand, retry, life
@Version: 3.6.4
@Date: 8/16/19
"""

import random
import time

#Error Finder
print("Welcome to the NumberGuesser! You will start out with 5 lives. ")
time.sleep(1.5)
def error():
    try:
        l = int(input("Take a guess and enter in a number: "))
        return l
    except:
        print("Error, numbers only!")
        return error()

#Guessing Detector
def checkNum(numb, rand):
      if(numb==rand):
          print("You got it right!Good job with your lucky guesses!")
          return True
      elif(numb < rand):
          print("Thats too low, guess higher.")
          time.sleep(.5)
          return False
      else:
          print("Thats too high, guess lower.")
          time.sleep(.5)
          return False

#Number Genertor with lives 
def game():
  num = random.randint(0,100)
  life = 5

  while (life>0):
        ans = error()
        if(checkNum(ans, num)):
              break
        else:
            life = life - 1
            print("You have " + str(life) + " lives left!")
            time.sleep(1)
        if life == 0:
            time.sleep(1)
            print("The number was",num, "but good try.")
            time.sleep(1.5)

#Play Again
  retry = input("Do you want to play again?")
  time.sleep(1.5)
  retry = retry.lower()
  if(retry in retrys):
      game()
  else:
        time.sleep(2)  
        print("Come back next time!")

retrys = {"yes", "ye", "y", "ok", "sure", "k", "yea"}
game()
