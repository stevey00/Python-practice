'''
when playing games where you have to roll two dice, it is nice to know the odds of each roll. For instance,
the odds of rolling a 12 are about 3%, and the odds of rolling a 7 are about 17%. You can compute these 
mathematically, but if you don't know the math, you can write a program to do it. To do this, your program 
should sumulate rolling two dice about 10,000 times and compute and print out the percentage of rolls that 
come out to be 2,3,5,...12.
'''

import random

def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def calculate_percentage(rolls, total):
    return (rolls / total) * 100

def main():
    rolls = {i: 0 for i in range(2, 13)}  # Initialize roll counts for each possible value
    total_rolls = 10000

    for _ in range(total_rolls):
        roll = roll_two_dice()
        rolls[roll] += 1

    print("Roll\tPercentage")
    for roll, count in rolls.items():
        percentage = calculate_percentage(count, total_rolls)
        print(f"{roll}\t{percentage:.2f}%")

if __name__ == "__main__":
    main()
