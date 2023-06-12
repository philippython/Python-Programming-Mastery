from typing import List
# def divide_numbers(num1, num2):
#     return num1 / num2

# result = divide_numbers(10, 2)
# print(result)

# -----------------------PART 1: Passed--------------------------
# def calculate_average(numbers: List):
#     total = 0
#     for number in numbers:
#         total += number
#     average = total / len(numbers)
#     return average

# print(calculate_average([1, 2, 3, 4]))
# ---------------------PART 2 : Passed-------------
# [9, 6, 7, 10, 4, 5]
# def find_largest(numbers):
#     largest = numbers[0] # 9, 6, 7
#     for number in numbers:
#         if number > largest:
#             largest = number
#     return largest

# print(find_largest([1, 2, 3, 4]))
# -----------------PART 3 ---------------------
# def main():
#     numbers = input("Enter a list of numbers, separated by commas: ")
#     numbers_chunk = numbers.split(',')
#     numbers_int = []

#     for num in numbers_chunk:
#         numbers_int.append(int(num))

#     average = calculate_average(numbers_int)
#     largest = find_largest(numbers_int)

#     print(f"Average: {average}")
#     print(f"Largest number: {largest}")

# main()

# def divide_numbers(a, b):
#     result = a / b
#     return result

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# result = divide_numbers(num1, num2)
# print("The result of the division is: " + str(result))