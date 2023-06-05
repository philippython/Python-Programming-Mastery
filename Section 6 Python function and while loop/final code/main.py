import random
# # declaring function
# def greeting():
#     # function body
#     # function dcstring: optional
#     """
#     this function prints a greet message in the console
#     it does not take any parameter and doesn't return any value
#     """

#     name = input("What is your name ")

#     greet_message = f"Hello {name}, Welcome this is my first python function"

#     print(greet_message)

# # calling the function greeting
# greeting()

# # dunder method / magic method
# # __doc__
# print(greeting.__doc__)

# def passer():
#     pass 
#     # pass keyword is a placeholder and it doesn't invoke ay action in our code


# passer()

# simple interest = principal * rate * time 
# at pooint of declaration pricipal, rate and time are parameters
# def simpleInterest(principal, rate, time):
#     """
#     this is a function to calculate simple interest
#     """
#     interest = ( principal * time ) * rate / 100
#     print(interest)

# at point of call pricipal, rate and time are arguments
# simpleInterest(7000, 5, 1)

# 1. Positional argument
# 2. keyword argument
# 3. default argument
# def ageCalc(name, birth_year=1998):
#     """ simple function to print your age and name"""
#     print(name)
#     print(birth_year)
#     age = 2023 - birth_year 
    # 2023 - "philip"
    # print(f"{name} is {age} years old!")

# ageCalc(name="philip", birth_year=2004)
# ageCalc("philip", 2004)
# ageCalc("philip", 2004)


# counter = 10

# while counter > 0 : condition for while loop
    # counter -= 1
    # print(counter)    code in he loop
    
# infinite loop

#  challenge 1: Factorial Calculator

# Write a Python function called factorial that calculates the factorial of a given number using a while loop. The factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. The factorial of 0 is defined to be 1.

# The function should have the following specifications:

# Name: factorial
# Parameters:
# n (integer): The number for which the factorial needs to be calculated.
# Return:
# result (integer): The factorial of the given number.
# You should use a while loop inside the function to calculate the factorial.


# def factorial(n):
#     result = 1
#     if n == 0 :
#         print(1)
#     else:
#         pass

    # implementing while loop
    # n = 3 // 3 *  2 * 1 // 1 * 2 * 3
    # while n > 1:
        # result *= n 5 * 1 * 4 * 3 * 2
#         n -= 1
#     print(result)

# factorial(4)
# 4 * 3 * 2 *

# Task 2: Create a simple game function, that takes no parameter and initiates the guessing game
# 1. The game should generate a random number between 1 and 100.
# 2. The player should be prompted to guess the number.
# 3. The game should provide feedback to the player after each guess, indicating whether the guess was too high or too low.
# 4. The player has 5 chances to get it right and whenever they guess wrong they lose a chance.
# 5. If the player guesses the correct number within the given attempts, they should be declared the winner.
# 6. If the player runs out of attempts without guessing the correct number, they should be declared the loser.
# Hint : Learn about python break keyword

game_logo = """
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▄▄█░██░█░▄▄█░▄▄█░▄▄███▄░▄█░████░▄▄███░▄▄▀█░██░█░▄▀▄░█░▄▄▀█░▄▄█░▄▄▀
█░█▄▀█░██░█░▄▄█▄▄▀█▄▄▀████░██░▄▄░█░▄▄███░██░█░██░█░█▄█░█░▄▄▀█░▄▄█░▀▀▄
█▄▄▄▄██▄▄▄█▄▄▄█▄▄▄█▄▄▄████▄██▄██▄█▄▄▄███▄██▄██▄▄▄█▄███▄█▄▄▄▄█▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
            """

total_chances = ['💖','💖','💖','💖','💖']
win_emoji = '🏆🎉'
lose_emoji = '💔😭'


def game():
    print(game_logo)

    # generating a random number beween 1 and 100
    correct_number = random.randint(1, 100)

    # initializing 
    while total_chances.count('💖') > 0:
        guessed_number = int(input("Guess a number between 1 and 100 "))

        if guessed_number > correct_number:
            total_chances.remove('💖')
            total_chances.append('💔')
            print(f"You Guess is too high, you have lost an attempt {total_chances}")
        elif guessed_number < correct_number:
            total_chances.remove('💖')
            total_chances.append('💔')
            print(f"You Guess is too Low, you have lost an attempt {total_chances}")
        else:
            print(f"You have gotten the correct number, You've won {win_emoji}")
            break
    
    if total_chances.count('💖') == 0: print(f"You're out of chances, You've lost {lose_emoji}") 

game()






