from typing import List
# colors = ("green", "blue", "red")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_number = [n**2 for n in numbers if n > 2 ]
# odd_number = [n for n in range(1, 16) if n % 2 != 0]
# colors_length = [len(color) for color in colors]

# for n in numbers:
#     if n % 2 == 0 :
#         even_number.append(n)

# print(numbers)        
# print(even_number)
# print(odd_number)
# print(colors_length)

# Dictionary comprehension
# prices = {'apple': 0.99, 'banana': 0.5, 'orange': 0.75, 'mango': 1.5, 'avocado': 2.99}
# expensive_prices = {fruit : price for fruit, price in prices.items() if price > 1.00}
# fruit_names = {fruit_name: len(fruit_name) for fruit_name in prices.keys() }

# names = ['Alice', 'Bob', 'Charlie', 'David', True, 67]
# names_dict = {name:len(name) for name in names if type(name) == str }

# # for name in names:
# #     names_dict[name] = len(name)
# print(fruit_names)
# print(expensive_prices)
# print(names_dict)
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def generator_function():
#     for n in range(1, 16):
#         if n % 2 != 0:
#             yield n

# odd_numbers = generator_function()
# generator expression
# odd_numbers = (n for n in range(1, 16) if  n % 2 != 0)
# print(odd_numbers)
# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))
# print(next(odd_numbers))

# odd_number = list(generator_function())
# print(odd_number)




# Task: Given a list of names, create a new dictionary that groups the names based on their first letter.
# The keys of the dictionary should be the first letters of the names, and the values should be lists of 
# names starting with that letter.

# Instructions:

# Write a function called group_names(names) that takes in a list of names as input.
# Inside the function, use a dictionary comprehension to create a new dictionary that groups the names based on their first letter.
# Return the resulting dictionary.
# Test your function with a sample list of names.

def group_names(names: List):
    """A function to group names into a dictionary based on first letter"""

    grouped_names = {name[0] : [ n for n in names if n.startswith(name[0])] for name in names}
    return grouped_names


contacts =  [
    'Emma',
    'Liam',
    'Olivia',
    'Noah',
    'Ava',
    'Isabella',
    'Sophia',
    'Jackson',
    'Lucas',
    'Mia',
    'Charlotte',
    'Harper',
    'Evelyn',
    'Alexander',
    'James',
    'Benjamin',
    'Henry',
    'Ella',
    'Emily',
    'Michael'
]

print(group_names(contacts))





