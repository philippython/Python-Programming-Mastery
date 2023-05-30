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
def ageCalc(name, birth_year=1998):
    """ simple function to print your age and name"""
    print(name)
    print(birth_year)
    age = 2023 - birth_year 
    # 2023 - "philip"
    print(f"{name} is {age} years old!")

# ageCalc(name="philip", birth_year=2004)
# ageCalc("philip", 2004)
ageCalc("philip", 2004)
















  










