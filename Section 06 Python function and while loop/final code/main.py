# declaring a function
# def greet():
#     """This function is a simple greet function"""
#     print("Hello, how are you doing!")

# calling the function
# greet()   
# to access the docstring of a python function functionname.__doc__ 
# print(greet.__doc__)

# def evenOdd():
#     num = int(input("enter a number"))
#     if num % 2 == 0 :
#         print("Number is even")
#     else:
#         print("number is odd")

# evenOdd()
# print(evenOdd.__doc__)

def age():
    # this function's logic is yet to be known
    birth_year = int(input("What is your birth year? "))
    age = 2023 - birth_year 
    if age > 18 :
        print(f"User is an adult, he/she is {age}")
    else:
        pass

age()













