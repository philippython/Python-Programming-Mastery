#  Arithnetic operators
# + , * , / , - , // , ** , %
bill = 5_000
tax = 200
salary = 100_000
# print(salary)

# addition operation
# total = bill + tax
# print(total)

# substraction operator
# differnce = bill - tax
# print(differnce)

# multiplication operation
# multiply = bill * tax
# print(multiply)

# division operation 
#  5000 / 200
# dividend = bill / tax
# print(dividend)

#  floor division operation
# 5000 // 200
# floor_dividend = bill //  tax
# print(floor_dividend)


# print(7 // 2)
# 3.5

# modulus operation
#  % 
# 5000 % 200
# 5000 / 200 = 25 
# fee = 5734


# mod_remain = fee % 200
# mod_divide = fee / 200
# print(mod_divide)
# print(mod_remain)
# 5734 / 200 = 28 remain 134
# 134 / 200
# modulus = bill % tax
# print(modulus)


# exponential operator
#  **
# initial = 9
# power = 3
# expo = initial ** power
# 9 ** 2 = 9 * 9 * 9
# print(expo)

# assignment operators
loan = 5700 
# equal to 

# +=
loan = loan + 300
# print(loan)

#  plus equal
loan += 300
# print(loan)

# substract equal -=
# loan -= 500
# print(loan)

# multiply equal
loan *= 2
# 5800 * 2
# print(loan)

# # divide equal 
# loan /= 2
# print(loan)


# floor divide equal
# loan //= 2
# print(loan)

loan = 70_000
repayment = 80_000

# comparisom operators
#  == , != , > , < , >= , <=

# equal equal ==
bill = 500
response = "yes"

# not equal !=
# if response != "yes":
#     print("User rejected admission")
# else:
#     print("User accepted admission")

# <= is combination of == and <
# if loan <= repayment:
#     print("User has completed repaying loan")
# else:
#     print("User is a debtor")
available_bullets = 12

# >= combination of > and ==

# if available_bullets >= 1 :
#     print("Keep shooting")
# else:
#     print("reloading...")

# if response == "no":
#     print("User Response is NO")
# else:
#     print("User response is yes")


# if bill == 500 :
#     print("Bill is accurate")
# else:
#     print("Bill is not accurate")

# if loan > repayment :
#     print("User is still owing")
# else:
#     print("Loan is repaid")

# grader
#  70 -> A
#  60 -> B
#  50 -> C
#  < 50 -> D

# score = int(input("what is your score"))

# if score >= 70 :
#     print("GRADE A")
# elif score >= 60 :
#     print("GRADE B ")
# elif score >= 50 :
#     print("GRADE C") 
# else:
#     print("GRADE D")

# logical operator
# and , or and not

#  Toilet management system 
# age = int(input("How old are you ? "))
# gender = input("Are you a male or female ? ")


# conditional statement
# if age >= 18 and gender == "male" :
#     print("Access granted into male club toilet")
# elif age >= 18 and gender == "female" : 
#     print("Access granted into female club toilet")
# elif age < 18 or gender == "female" : 
#     print("Public female toilet outside the club")
# elif age < 18 or gender == "male" :
#     print("Public male toilet outside the club")

# inverse a boolean True and False
# not True - > False
#  not False -> True

# print(not False)


# number checker

# number = int(input("Enter a number "))

# # outer if statement
# if number < 0 :
#     print("Number is negative")
# else:
#     # inner if statement
#     if number == 0 :
#         print("Number is zero")
#     else:
#         print("Number is positive")

# is_hungry = input("Are you hungry? ")

# if is_hungry == "yes" :
#     print("Go to grocery store")
#     # inner if..else condition 
#     cost = float(input("How much does a chocolate cost ?"))
#     if cost <= 1 :
#         print("Buy 3 chocolates")
#     else :
#         print("Buy 1 choclate")
# elif is_hungry == "no":
#     print("Stay at home")
#     interested_in_game = input("Do you want to play fortnite? ")
#     # first inner if.. else conditional statement
#     if interested_in_game == "yes":
#         print("See you next week")
#     elif interested_in_game == "no":
#         print("Go back to study")
#         # creating another input function
#         fav_subject = input("What is your favorite subject? ")
#         # inner if..else statement conditional statement
#         if fav_subject == "computer science" :
#             print("That is my favorite subject")
#         else : 
#             print("We have nothing in common")
# else:
#     print("Invalid Reponse")


# solution to football admin project
# match_status = input("What is the status of the match? ")

# if match_status == "suspended" :
#     print("Match suspended")
# elif match_status == "played":
#     home_goals = int(input("How many goals was scored by the home team? "))
#     away_goals = int(input("How many goals was scored by the away team? "))
#     if home_goals > away_goals:
#         print("Home team won the match")
#     elif home_goals == away_goals :
#         print("The match was a draw")
#     else:
#         print("Away team won the match")
# else:
#     print("Invalid match status")

# minutes to hours converter
minutes = float(input("How many minutes would you like to convert to hours"))

# floor divide 
hours = minutes // 60 # 372.5 // 60 = 6.325
mins = minutes % 60 # 372.5 / 60 372.5 / 60 = 6
# 60 * 6 = 360 12.5 


response = f"{hours}hrs {mins}mins"
print(response)
# float datatype
# 360mins -> 6 hrs
# 372.5 mins -> 6 hrs ...mins
# 6 hrs 30mins 













































