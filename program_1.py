# Programmer: Austin Long
# Date: 2025-02-26
# Program: Random Dice

import random

# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.

# Adds two random dice together and returns the result
def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

    # Sum 2 numbers
    dice_sum = dice_1 + dice_2

    # return sum to calling function
    return dice_sum

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
def main():
    # Number of times to roll
    num_rolls = 100

    # Sum of all rolls
    roll_sum = 0

    # Sum up all rolls
    for _ in range(num_rolls):
        roll_sum += randDice()

    # Calculate average
    average = roll_sum / num_rolls

    # This also works:
    # average = sum((randDice() for _ in range(num_rolls))) / num_rolls

    # Display results
    print(average)


if __name__ == "__main__":
    main()
