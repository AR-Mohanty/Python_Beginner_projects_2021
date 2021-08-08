# Task: Below are the steps:
#
# ->Build a Number guessing game, in which the user selects a range.
# ->Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
# ->Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses

import random
import math

lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))

x = random.randint(lower_bound,upper_bound)
print('\n\tYou have only', round(math.log(upper_bound - lower_bound + 1, 2)), " Chances to guess the integer!\n")

count = 0

while count < math.log(upper_bound - lower_bound +1,2):
    count += 1
    guess = int(input("guess number:- "))

    if x == guess:
        print("Congratulations you dit it in ",count," try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("you guessed too high!")

if count >= math.log(upper_bound - lower_bound +1,2):
    print(f"The number is {x}")
    print("Better luck next time!")