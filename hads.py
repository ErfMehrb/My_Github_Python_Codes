from ast import Break
from ast import Continue
import random
i = 1
j=99
while True:

  guess = random.randint(i,j)
  print(guess)
  status = input("Please Clarify the status of guessed Number with k,b or d      ")
  if status == "k":
    j = guess
    continue
  if status == "b":
    i = guess
    continue
  if status == "d":
    print(" your guess is correct!!")
    break