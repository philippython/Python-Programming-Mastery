import csv 
# intro = open("final code/intro.txt", "r")
# print(intro.read()) 

# intro.close()

# with open("final code/intro.txt", "r") as file :
#     print(file.read())
#     print(file.readline())
#     print(file.readline())
#     print(file.readline())

# with open("stater code/test.txt", "x") as test_file:
#     pass


# with open("final code/intro.txt", "w") as new_file:
#     new_file.write("I live in Ogun state, Nigeria")

# with open("final code/intro.txt", "a") as updated_file:
#     updated_file.write("I'm philip\nA python engineer\nI'm 19 yrs old")

data = [
    ['Name', 'Age', 'City'],
    ['John', 25, 'New York'],
    ['Alice', 30, 'London'],
    ['Bob', 35, 'Paris']
]

# writing into a csv file
# with open("final code/data.csv", "w") as data_file:
#     writer = csv.writer(data_file)
#     writer.writerows(data)
#     writer.writerow(['Johnny', 20, 'Florida'])

# reading from a csv file
with open("final code/data.csv", "r") as data_file:
    reader = csv.reader(data_file)
    
    for row in reader:
        print(row)














