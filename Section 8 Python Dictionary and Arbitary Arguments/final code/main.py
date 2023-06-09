# dict constructor function
# created a python dictionary
# bank_users = dict()
# bank_users_v2 = {}
# age = 19
# colors = ("red", "blue", "yellow")
# bools = {True, False}


# bools.add("BOOL")
# print(bools)
# adding items into a python dictionary
# key: name , value: balance
# bank_users["Philip"] = 200
# bank_users["Philips"] = 320
# bank_users["chris"] = 4900
# bank_users[age] = "2004"
# bank_users[colors] = "RBY"
# bank_users[bools] = "Boolean"
# allowed dictionary key datatype numeric(int, float), string , set , tuple -> immutable

# {'Philip': '$200USD', 'Philip': '$320USD'}
# keys must be immutable and unique

# modifying/updating values with a python dictionary
# chris_bal = bank_users["chris"]
# philip_bal = bank_users["Philip"]

# bank_users["chris"] = chris_bal - 900

# del bank_users["Philips"]
# print(bank_users)


# print(type(bank_users_v2))


# stock = {
#     "electronics": 45,
#     "furniture": 90,
#     "books": 12,
#     "macbook": 3
# }

# numbers = [1, 2, 3]
# print(stock["macbook"])
# print(stock.get("electronics"))

# keys and values 
# print(stock.keys())
# print(stock.values())

# clear and copy
# stock.clear()
# stock_2 = stock.copy()
# print(stock)
# print(stock_2)

# for num in numbers:

# for key, value in dictionary.items():
# print(stock.items())

# # looping through dict items
# for item, count in stock.items():
#     print(item)
#     print(count)

# # looping through dict keys
# for key in stock.keys():
#     print(key)

# # looping through dict keys
# for value in stock.values():
#     print(value)

# popped_item = stock.pop("furniture", "key is invalid")
# print(popped_item)
# print(stock)
# students_1 = {"philip": 4.14, "hassan": 4.23}
# students_2 = {"jamiu": 2.78, "farouq": 3.00}

fruit_categories = {
    'fruit': {
        'apple': {
            'color': 'red',
            'taste': 'sweet'
        },
        'banana': {
            'color': 'yellow',
            'taste': 'sweet'
        }
    },
    'vegetable': {
        'carrot': {
            'color': 'orange',
            'taste': 'crunchy'
        },
        'spinach': {
            'color': 'green',
            'taste': 'bitter'
        }
    }
}

# Spinach is a vegetable it has a bitter taste and it's green in color

def describe_fruit(fruit_name: str, fruits: dict) -> str:

    for category, values in fruits.items():
        for fruit, property in values.items():
            if fruit_name == fruit:
                color = property.get("color")
                taste = property.get("taste")
                print(f"{fruit_name} is a {category} it has a {taste} taste and it's {color} in color")
            

describe_fruit("carrot", fruit_categories)
describe_fruit("apple", fruit_categories)
describe_fruit("banana", fruit_categories)
describe_fruit("spinach", fruit_categories)
describe_fruit("orange", fruit_categories)





























# merge 1: 
# students_1.update(students_2)
# print(students_1)

# merge 2:
# total_students = {**students_1, **students_2}
# print(total_students)

