# intro = open("final code/intro.txt", "r")
# print(intro.read()) 

# intro.close()

with open("final code/intro.txt", "r") as file :
    print(file.read())
    print(file.readline())
    print(file.readline())
    print(file.readline())

with open("stater code/test.txt", "x") as test_file:
    pass


with open("final code/intro.txt", "w") as new_file:
    new_file.write("I live in Ogun state, Nigeria")

with open("final code/intro.txt", "a") as updated_file:
    updated_file.write("I'm philip\nA python engineer\nI'm 19 yrs old")






















