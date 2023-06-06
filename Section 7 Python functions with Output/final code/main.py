import random
# def calculate_average(numbers):
#     """
#     calculates average of numbers in a list
#     """

#     sum = 0

#     for num in numbers:
#         sum += num

#     average = sum / len(numbers)
#     print("I am a string within calculate_average function")
#     print("I am a print function after the return statement")
#     return average
    

# ages = [45, 56, 55, 43, 49]

# avg = calculate_average(ages) # caller : returned value is assigned to the caller

# def order_pizza():
    # Gather everyone's pizza preferences
    # iron_man = "Pepperoni"
    # captain_america = "Cheese"
    # thor = "Meat Lovers"
    # hulk = "Veggie Supreme"

    # Calculate the total number of pizzas needed
    # total_pizzas = 4

    # Calculate the size of each pizza based on the number of people
    # pizza_size = total_pizzas * 8

    # Assemble the team's preferences into a list
    # team_preferences = [iron_man, captain_america, thor, hulk]

    # Return multiple values as a tuple
    # return pizza_size, team_preferences, "successfully ordered"

# Call the function to get the results
# pizza_size, preferences = order_pizza()
# orderPizza = order_pizza()
# pizzaSize , pizzaPreferences , orderStatus = orderPizza
# print(pizzaSize)
# print(pizzaPreferences)
# print(orderStatus)


# print(avg)

# def display_info(name: str, age: int, height: float) -> str:
#     """
#     a function that displays a person's info
#     """

#     return f"Name : {name}, Age: {age}, height: {height}"

# info = display_info("Philip", 19, 1.45)
# print(display_info("Philip", 19, 1.45))
# print(info)

# game_logo = """
# ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
# █░▄▄▄█░██░█░▄▄█░▄▄█░▄▄███▄░▄█░████░▄▄███░▄▄▀█░██░█░▄▀▄░█░▄▄▀█░▄▄█░▄▄▀
# █░█▄▀█░██░█░▄▄█▄▄▀█▄▄▀████░██░▄▄░█░▄▄███░██░█░██░█░█▄█░█░▄▄▀█░▄▄█░▀▀▄
# █▄▄▄▄██▄▄▄█▄▄▄█▄▄▄█▄▄▄████▄██▄██▄█▄▄▄███▄██▄██▄▄▄█▄███▄█▄▄▄▄█▄▄▄█▄█▄▄
# ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
#             """

# win_emoji = '🏆🎉'
# lose_emoji = '💔😭'


# def game():
#     total_chances = ['💖','💖','💖','💖','💖']
#     print(game_logo)

#     # generating a random number beween 1 and 100
#     correct_number = random.randint(1, 100)
#     print(correct_number)

#     # initializing 
#     while total_chances.count('💖') > 0:
#         guessed_number = int(input("Guess a number between 1 and 100 "))

#         if guessed_number > correct_number:
#             total_chances.remove('💖')
#             total_chances.append('💔')
#             print(f"You Guess is too high, you have lost an attempt {total_chances}")
#         elif guessed_number < correct_number:
#             total_chances.remove('💖')
#             total_chances.append('💔')
#             print(f"You Guess is too Low, you have lost an attempt {total_chances}")
#         else:
#             print(f"You have gotten the correct number, You've won {win_emoji}")
#             break
    
#     if total_chances.count('💖') == 0: print(f"You're out of chances, You've lost {lose_emoji}") 

#     play_again = input("Would you like to play again? Y or N? ")
#     if play_again == "Y":
#         game()
#     else:
#         pass


# game()


# from typing import List

# def divisor(numbers : List):
    # """
    # simple function that divides numbers in a list by 2
    # """
    # result = []
    # for num in numbers :
    #     new_num = num / 2
    #     result.append(new_num)

    # return result

# def divisor_gen(numbers : List):
    # """
    # simple function that divides numbers in a list by 2
    # """
    # for num in numbers :
    #     yield num / 2


# weights = [90, 56, 43, 67, 34]
# calling normal function 
# weights_halved = divisor(weights)
#  calling generator function
# gen_function = divisor_gen(weights)
# yield_1 = next(divisor_gen(weights))
# print(yield_1)
# print(next(gen_function))
# print(next(gen_function))
# print(next(gen_function))
# for y in gen_function:
#     print(y)

# first-class function
# def dog_sound():
#     return "Woof!"

# def cat_sound():
#     return "Meow!"

# bullDogSound = dog_sound
# print(bullDogSound())
# animal_sounds = [dog_sound, cat_sound]  # We can store functions in a list

# for animal_sound in animal_sounds:
#     print(animal_sound())  # We can call the functions stored in the list

# Higher-order function
# def identify_animal_sound(animal_sound):
#     if animal_sound() == "Woof!":
#         print("The animal is a Dog")
#     else:
#         print("The animal is a cat")


# identify_animal_sound(cat_sound)
# identify_animal_sound(dog_sound)


# global scope
# duel_1 = "Gandalf vs Dumbledore"

# def magic_duel():
    # local scope
#     duel_2 = "Harry vs Voldemort"
#     print("I am a global variable", duel_1)
#     print("The winner is", duel_2)

# magic_duel()
# print(duel_1)
# print("The ultimate duel is", duel_1)

# x = 50

# def example():
    # x = 100
#     global x
#     x += 56
#     print("I am variable x in the local scope", x)

# example()
# print("I am a variable x on a global scope", x)

# def superhero_name():
#     print("I am a function in the global scope")

#     def get_secret_identity():
#         print("I am a function in the local scope")

#     get_secret_identity()
    

# superhero_name()

# def outscoped(param):
#     pass

# parent function
# def greet(lang: str): 
#     # child function 
#     def greeting(name: str) -> str:
#         if lang == 'english':
#             return f"Hello, {name}!"
#         elif lang == 'french':
#             return f"Bonjour, {name}!"
#         elif lang == 'spanish':
#             return f"Hola, {name}!"
#         else:
#             return f"Sorry, I don't know how to greet in {lang}."

#     return greeting


# greetOne = greet("spanish")
# greetingOne = greetOne("Philip")
# print(greetingOne)

# variable = 34

# def pet_counter(pet_owner):

#     pet_name = "Buddy"
#     count = 0

    # def counter():
    #     # enclosing scope
    #     nonlocal count
    #     count += 1
    #     print(f"Pet owner: {pet_owner}, {pet_name} has been called {count} time")

    # return counter


# buddy_count = pet_counter("Philip")

# for i in  range(4):
#     print(buddy_count())

# Shopping Cart Discount challenge

# The task involves creating a discount calculator function that calculates the discounted cost of a shopping cart based 
# on a given discount percentage. The function takes the discount percentage as input and returns another function, which 
# can be used to calculate the discounted cost of a list of items in the shopping cart.

# Inside the returned function, the total cost of the items is calculated by summing up the individual costs.
# Then, the discount amount is calculated by multiplying the total cost with the discount percentage and dividing 
# it by 100. The discounted cost is obtained by subtracting the discount amount from the total cost.

# The returned function also prints a message, thanking the user for choosing a specific shopping mall 
# (e.gThanks for choosing  "Walmart"). Finally, the discounted cost is returned as the output of the function
# from typing import List

# def discount_calculator_percentage(discount_percentage: float):
#         shoppingmall_name = "walmart"

#         def calculate_discount_price(items: List):
#             total = sum(items) 
#             discount_amount = total * discount_percentage / 100
#             discounted_cost = total - discount_amount
#             print(f"You have enjoyed a discount of {discount_percentage}, the total cost is {total} and the discounted cost is {discounted_cost}")
#             print(f"Thanks for chossing {shoppingmall_name}")
#             return discounted_cost
        
#         return calculate_discount_price
        
# cart = [67.90, 678, 450, 34]

# discount_ten_percent = discount_calculator_percentage(10)
# discount_price_on_10 = discount_ten_percent(cart)
# print(discount_price_on_10)