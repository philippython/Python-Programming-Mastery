# import bank
# import modulename

# from bank import  all_users as alu
# renamed the varibale name to alu

# all_users = ["thomas", "chris", "shadrach"]

# print(alu)
# print(all_users)

import random
import bank 
import string 
# from bank import all_users

# random.shuffle(scores)
# print(scores)

# seed function
# random.seed(7) # seed value
# winner = random.choice(names)
# print(winner)
# random_votes = random.randint(70, 100)
# print(random_votes)

#  choice , random , randint , shuffle, randbytes , seed
# random_score = random.choice(scores)
# print(random_score)
# iterable

# random_float = random.random()
# print(random_float)

# random_integer = random.randint(4, 10)  # 4 -> 10
# print(random_integer)

# creating a list
# first_list = []
# print(type(first_list))

# first_list = list()
# print(first_list)

# class_list = ["chris", "philip", "thomas", "shadrach"] # positive indexing -> [0 , 1 , 2 , 3]
#            negative indexing - > [-4 ,-3,-2,-1]
# accessing items in a list 
# first_item  = class_list[0]
# print(first_item)
# indexing 

# programming_lngs = ["Java", "C++", "Javascript", "Python", "C", "C#"] # [0, 1 , 2, 3, 4, 5] 6 - 1
# first_item = programming_lngs[0] 
# fourth_item = programming_lngs[3]
# print(first_item)
# print(fourth_item)

# C_sharp = programming_lngs[-1]
# print(C_sharp)

# programming_lngs[-1] = ".NET"

# print(programming_lngs)
# position on list - 1 
#  firstpostion = 1   sixthposition = 6
# 1- 1 = 0   6 -1 = 5
# len function
# total_lngs = len(programming_lngs)
# print(total_lngs)

# # indexerror
# item  = programming_lngs[10]
# print(item)

# sequence = [True, "John", [56, 78], "chris" , [True, ["shadrach", "John",78] , 90.66]]


# last_item = sequence[-1]
# nested_item = last_item[1]
# last_item_of_nested_list = nested_item[-1]
# print(last_item)
# print(nested_item)
# print(last_item_of_nested_list)

# print(sequence[-1][1][-1])

# cart = ["Macbook", "airpod", "toilet paper", "baking powder"]
# sub_cart = ["monitor", "keyboard"]
# scores = [50, 66, 3, 6, 32]

# scores.sort()
# print(scores)
# dir function 
# list_operations = dir(cart)
# print(list_operations)

# append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# cart.append("oven")
# cart.append("baking powder")
# cart.append(sub_cart)

# cart.extend(sub_cart)
# cart.insert(0, "rice")

# ['rice', 'Macbook', 'airpod', 'toilet paper', 'baking powder', 'oven', 'baking powder', 'monitor', 'keyboard']
# cart.pop(4)
# cart.remove("toilet tissue")
# cart.reverse()
# cart.sort()
# print(cart)


# index = cart.index("keyboard")
# print(index)
# print(cart[7])


# cart.clear()

# shallow_cart = cart.copy()
# print(shallow_cart)
# total_items = len(cart)
# no_of_items = cart.count("baking powder")
# print(total_items)
# print(no_of_items)

# careers = ["Frontend developer", "Backend Developer"]
# name = "philip" # ['p', 'h', 'i', 'l' , 'i' , 'p']
# language = "ENGLISH"
# names = "philip|shadrach|tobias|chris|john"

# split function 
# splitted_names = names.split("|")
# print(splitted_names)
# # upper function
# upper_name = name.upper()
# print(upper_name)

# # lower function
# lower_language = language.lower()
# print(lower_language)

# title_name = name.title()
# print(title_name)
# modified_name = name.replace("p", "f")
# print(modified_name)
# index = name.index("p")
# print(index)


# functions_of_list = dir(careers)
# print(functions_of_list)

# fumctions_of_string = dir(name)
# print(fumctions_of_string)

# capitalize, count, endswith, startswith, index, replace , title, upper ,lower, split, islower, isupper
# if name.endswith("k"): # True or False:
#     print("Name ends with charcter k")
# else:
#     print("Name does not end with charcter k")
# capitalizzed_name = name.capitalize()
# print(capitalizzed_name)

# char_count = name.count("p")
# print(char_count)

# countries_in_europe = ["Poland", "United Kingdom" ,"Wales", "Ireland", "Greece", "Germnay", "France" ] 
# if "O" in fullname:
#     print("Name contains char O")
# else:
#     print("Name does not contain character O")

# country = input("Name of country: ")


# if country not in countries_in_europe :
#     print("country is not an european country")
# else:
#     print("country is an european country")


#  memebership operator
# not in , in 

# if country in countries_in_europe :
#     print(f"{country} is an european country")
# else:
#     print(f"{country} is not an european country")

# import random

# print("Welcome back to the car chooser Program!!")

# # step 1 : get string of cars
# cars = input("Enter names of cars seperated by comma and a space ")

# # step 2 : split the string using the split() function
# list_of_cars = cars.split(", ")

# # step 3 : choose a random car from the list of cars
# random_car = random.choice(list_of_cars)

# #  step 4 : prin the random car
# print(f"You should get a {random_car}")
