# e_commerce = ("shopify", 'amazon', "ebay", "ebay")

# tuple_functions = dir(e_commerce)
# print(tuple_functions)

# item_count = e_commerce.count("ebay")
# print(item_count)

# index = e_commerce.index("amazon")
# print(index)
# e_commerce[-1] = "Klipkart"

# e_commerce_type = type(e_commerce)
# print(e_commerce_type)

# shopify = e_commerce[0]
# print(shopify)

# career = ("DeVops", "Software Developer", "teacher")
# continents = ("africa", "europe", "asia", "south america", "north america")

# simple
# tech_career_1 , tech_career_2, non_tech_career = career
# print(tech_career_1)
# print(tech_career_2)
# print(non_tech_career)

# afr , eur, asia, *amr = continents
# print(afr)
# print(eur)
# print(asia)
# print(amr)
# scores = {10, 49, 67 , 20 , 10 , 10}
# print(scores)
# sports = set()
# commerce = {"economics", "english", "maths", "commerce"}
# stem = {"science", "maths", "physics", "english"}

# union_courses = commerce.union(stem)
# print(union_courses)

# update method
# commerce.update(stem)
# print(commerce)

# common_courses = commerce.intersection(stem)
# print(common_courses)

# print(stem)
# sets_methods = dir(stem)
# print(sets_methods)
# print(sports)
# print(type(sports))
# sports.add("football")
# sports.clear()
# copy_sports = sports.copy()
# print(copy_sports)
# print(sports)
# 'add', 'clear', 'copy', 'difference', 'discard', 'intersection', 'pop', 'remove', 'union', 'update'
# vowels = {"a", "e", "i", "o", "u"}
# alphabets = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j" , "k" ,"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x","y","z"}


# vowels.remove("b")
# print(vowels)
# vowels.pop()
# print(vowels)
# common = alphabets.intersection(vowels)
# print(common)
# vowels.discard("b")
# print(vowels)

# # alphabets - vowels
# difference = alphabets.difference(vowels)
# print(difference)

# # vowels - alphabets
# diff_2 = vowels.difference(alphabets)
# print(diff_2)

currrency = ["USD", "EURO", "POUNDS", "NAIRA", "RUPEES"]
countries = ("United states", "Germany", "United kingdom", "Nigeria", "Indian")
developers = {"chris", "shadrach", "philip", "Tobias"}
email = "johndoe@gmail.com"

# for curr in currrency:
#   print(curr)

# for country in countries:
#   print(country.upper())

# for dev in developers :
#   # print(dev)
#   # logic : print length of the dev name
#   len_of_name = len(dev)
#   print(f"{dev} is {len_of_name} characters long")

for char in email:
    print(char)






















# fizzbuzz    
# fuzz = [1, 2,3 ,4,5,6,7,8,9,10,11,12,13,14,15]

# step 1 : iterate over list
# for num in fuzz :
  # step 2 : check if current number is divisible by 3 or 5
  # num = 6 
  #  6 % 3 = 0
  # if num % 3 == 0 :
  #   print("fizz")
  # elif num % 5 == 0 :
  #   print("buzz")
  # else:
  #   print(num)

# terms = [67, 43, 24, 45, 22]

# sum of terms / total no of terms
# step 1 : sum up all terms
# sum_of_terms = 0
# for num in terms:
#   sum_of_terms += num
  

# step 2 : get total no  of terms
# no_of_items = len(terms)
# step 3 : divide sum of terms by total no of terms
# result = sum_of_terms / no_of_items
# print(result)


# range function with start and stop parameter
# for num in range(29, 34):
#   print(num)

# range function without a start parameter
# for number in range(7):
#   print(number)

# range functtion wuith all parameters: start , stop, step
# for num in range(2,15,3):
#   print(num)


# 2233 6789 6543 0534

# step 1 : Get user's debit card number
# card_num = input("Enter your 16 digit debit card number seperate each 4 digit by a space ").replace(" ", "")

# step 2 : loop through debit card number 
# counter = 0 
# card_number = ""

# for num in card_num:
#   counter += 1
  # step 3 : represent first 12 digits by *
  # if counter <= 12:
  #   card_number += "*"
  # step 4 : leave last 4 digits of the debit card number
  # else:
  #   card_number += num

# print(card_number)
# step 5 : join step 3 + step 4
# step 6 : print the formatted debit card digits










































