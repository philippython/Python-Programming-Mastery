import math
from functools import reduce
import re 
# lambda parameters : expression 
# simple_interest = lambda p , r , t : p * r * t / 100

# print(simple_interest(4500, 5, 2))

# def discount_calculator_percentage(discount_percentage: float):
#         shoppingmall_name = "walmart"

#         return lambda items : f"You have enjoyed a discount of {sum(items) * discount_percentage / 100} the total cost is {sum(items)} and the discounted cost is {sum(items) - (sum(items) * discount_percentage / 100)} \nThanks for shopping at {shoppingmall_name}"
        # def calculate_discount_price(items: List):
        #     total = sum(items) 
        #     discount_amount = total * discount_percentage / 100
        #     discounted_cost = total - discount_amount
        #     print(f"You have enjoyed a discount of {discount_percentage}, the total cost is {total} and the discounted cost is {discounted_cost}")
        #     print(f"Thanks for chossing {shoppingmall_name}")
        #     return discounted_cost
        
        # return calculate_discount_price
        
# cart = [67.90, 678, 450, 34]
# discount_percent = discount_calculator_percentage(10)
# print(discount_percent(cart))
# discount_ten_percent = discount_calculator_percentage(10)
# discount_price_on_10 = discount_ten_percent(cart)
# print(discount_price_on_10)

# def operation(operation_type, a, b):
#     return operation_type(a, b)

   # multiply = lambda x , y : x * y

# print(operation(multiply, 3, 5))

bank_transactions = [90.96, 67.45, 78.90, -23.67, 45.00, -700, 340.13, 56.8, 89]

# saving = savings = list(map(lambda transaction : math.floor(transaction * 5 / 100) if transaction > 1.0 else 0, bank_transactions))
# savings = list(map(lambda transaction : round(transaction * 5 / 100, 2) if transaction > 1.0 else 0, bank_transactions))
# print(saving)   
# print(savings)
# filtered_savings = list(filter(lambda saving : saving != 0, savings))
# print(filtered_savings)
# total_savings = round(reduce(lambda prev, next : prev + next,  filtered_savings), 2)
# print(total_savings)

# Sales data for different products
# sales_data = [
#     {"product": "Apple", "quantity": 5, "price": 2.5},
#     {"product": "Banana", "quantity": 10, "price": 1.75},
#     {"product": "Orange", "quantity": 8, "price": 3.0},
#     {"product": "Grapes", "quantity": 3, "price": 4.25},
#     {"product": "Mango", "quantity": 6, "price": 2.0},
# ]

# Chaining array methods: map, filter, reduce
#  filter -> map -> reduce 
# total_revenue = reduce(lambda prev, next : prev + next , list(map(lambda sales : sales["quantity"] * sales["price"], \
#                     list(filter(lambda data : data["product"] != "Grapes", sales_data))
#                 )))
# print(total_revenue)

# sentence = "I'm Philip and i would be the best\nI'm 19"
# print(sentence[4:10])
# pattern = re.compile(r"i", flags=re.I)
# pattern = re.compile(r".", flags=re.DOTALL)
# pattern = re.compile(r"19$")


# matches = pattern.finditer(sentence)

# for match in matches:
#     print(match)

# string and raw string
# print("\tMy name is philip\nI'm 19")
# print(r"\tMy name is philip\nI'm 19")
# with open(r"Section 15 Array methods and Python regex\final code\text.txt", "r") as text:
#     contents = text.read()
    # pattern = re.compile(r"\B@\w{7,15}")
    # pattern = re.compile(r"https?://(www.)?\w+.com")
    # pattern = re.compile(r"[+]\d{1,3}\s\d{3}-\d{3}-\d{4}")
    # pattern = re.compile(r"[a-zA-Z0-9+-_].[0-9].[0-9].[0.9]")
    # pattern = re.compile(r"\w{1,3}[.]\w{1,3}[.]\w{1,3}[.]\w{1,3}")
    # pattern = re.compile(r"(Mr|Mrs|Ms)\s[A-Z]\w+")
    # pattern = re.compile(r"[a-zA-Z0-9+-_.]+@[a-z]+(.com|.edu)")

    # matches = pattern.finditer(contents)
    # for match in matches:
    #     print(match)


# Your task is to create a sentimental analysis tool using regular expressions (regex)
# The tool should analyze a given text and determine the sentiment (positive, negative, or neutral) based on certain 
# patterns or keywords present in the text.
# Implement the function to perform sentimental analysis on the given text using regular expressions. Follow these steps within the function:
# a. Create a regex pattern to match positive sentiment keywords (e.g., "good," "great," "amazing," etc.). You can use the pipe (|) operator to specify multiple keywords in the pattern.
# b. Create another regex pattern to match negative sentiment keywords (e.g., "bad," "terrible," "awful," etc.).
# c. Use the re.findall() function to find all matches of positive and negative sentiment keywords in the text.
# d. Determine the sentiment based on the number of matches:

# If there are more positive matches than negative matches, return "Positive sentiment."
# If there are more negative matches than positive matches, return "Negative sentiment."
# If the number of positive and negative matches is the same, return "Neutral sentiment."
# Test your function with different text inputs to ensure it provides the correct sentiment analysis.
# example texts
# This movie is really good!
# I had a terrible experience.
# The weather is okay.

def sentiment_analysis(text: str):
    """This function returns Positive, negative or neutral sentitment"""
    positive_pattern = re.compile(r"(good|great|amazing|awesome)",flags=re.I)
    negative_pattern = re.compile(r"(bad|terrible|awful)",flags=re.I)

    positive_matches = re.findall(positive_pattern, text)
    negative_matches = re.findall(negative_pattern, text)

    if len(positive_matches) > len(negative_matches):
        return "Positive sentiment"
    elif len(positive_matches) < len(negative_matches):
        return "Negative sentiment"
    else:
        return "Neutral sentiment"


print(sentiment_analysis("This movie is really good!"))
print(sentiment_analysis("I had a terrible experience."))
print(sentiment_analysis("The weather is okay."))














