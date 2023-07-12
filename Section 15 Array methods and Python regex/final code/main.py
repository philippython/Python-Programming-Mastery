import math
from functools import reduce
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
sales_data = [
    {"product": "Apple", "quantity": 5, "price": 2.5},
    {"product": "Banana", "quantity": 10, "price": 1.75},
    {"product": "Orange", "quantity": 8, "price": 3.0},
    {"product": "Grapes", "quantity": 3, "price": 4.25},
    {"product": "Mango", "quantity": 6, "price": 2.0},
]

# Chaining array methods: map, filter, reduce
#  filter -> map -> reduce 
total_revenue = reduce(lambda prev, next : prev + next , list(map(lambda sales : sales["quantity"] * sales["price"], \
                    list(filter(lambda data : data["product"] != "Grapes", sales_data))
                )))
print(total_revenue)
            














# for transaction in bank_transactions:
#         # code here




















