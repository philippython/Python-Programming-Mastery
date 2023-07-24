import json
# with open(r"Section 17 Python Error exceptions & Json module\final code\patterns.txt", "r") as patterns:
#     print(patterns.read())

# try :
#     # code that might not work
#     with open(r"Section 17 Python Error Handling , exceptions & Json module\final de\patterns.txt", "r") as patterns:
#         pass
# except FileNotFoundError:
#     # exception to be caught
#     with open(r"Section 17 Python Error Handling , exceptions & Json module\final code\intro.txt", "w") as intro:
#         intro.write("Hello i am inside the except block of the try-except block - updated")
# else:
#     # code that should be execute if nothing
#     patterns.read()
# finally:
#     # code to be executed regardless of if there is an exception or not
#     print("I'm a string in the finally block of this try-except block i would get executed regardless of what goes wrong")

# def square_root(num):
#     if num < 0 :
#         # raise error
#         raise ValueError("Cannot get square root of a negative number")
#     else:
#         return num ** 0.5


# print(square_root(4))
# print(square_root(-2))

data = {
  "name": "John Doe",
  "age": 30,
  "city": "New York",
  "email": "johndoe@example.com",
  "hobbies": ["reading", "traveling", "cooking"],
  "education": {
    "degree": "Bachelor's",
    "major": "Computer Science",
    "university": "ABC University"
  },
  "is_employed": True
}

# encoding/serializing
# json_data = json.dumps(obj=data, indent=4)
# # print(json_data)

# #  decoding/deserializing
# deserialized_data = json.loads(json_data)
# print(type(deserialized_data))


# save an encoded json
# try: 
#     with open(r"Section 17 Python Error Handling , exceptions & Json module\final code\data.json", "x") as data_file:
#         pass
# except FileExistsError:
#     with open(r"Section 17 Python Error Handling , exceptions & Json module\final code\data.json", "w") as data_file:
#         json.dump(obj=data, fp=data_file, indent=4)
# else:
#     with open(r"Section 17 Python Error Handling , exceptions & Json module\final code\data.json", "w") as data_file:
#         json.dump(obj=data, fp=data_file, indent=4)


# with open(r"Section 17 Python Error Handling , exceptions & Json module\final code\data.json", "r") as file:
#     loaded_json = json.load(fp=file)
#     print(type(loaded_json))

# with open(r"Section 17 Python Error Handling , exceptions & Json module\final code\store_data.json", "r") as store_data:
#     data = json.load(store_data)
    

#     electronics = data["store"]["departments"][0]["categories"][-1]["products"][1]
#     print(electronics)










































