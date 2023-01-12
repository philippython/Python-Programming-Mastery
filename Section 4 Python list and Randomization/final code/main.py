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

programming_lngs = ["Java", "C++", "Javascript", "Python", "C", "C#"] # [0, 1 , 2, 3, 4, 5] 6 - 1
first_item = programming_lngs[0] 
fourth_item = programming_lngs[3]
print(first_item)
print(fourth_item)

# position on list - 1 
#  firstpostion = 1   sixthposition = 6
# 1- 1 = 0   6 -1 = 5
# len function
total_lngs = len(programming_lngs)
print(total_lngs)

# indexerror
item  = programming_lngs[10]
print(item)