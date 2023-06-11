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
import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Pacman Game")
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)  # Turn off screen updates

# Create the maze
maze = [
    "*********************",
    "*                   *",
    "* ********* ******* *",
    "* *       * *       *",
    "* * ***** * * ***** *",
    "* * *         *     *",
    "* * * ********* *** *",
    "*   *       *       *",
    "***** ***** * *******",
    "*   *   *   *       *",
    "* *** *** ********* *",
    "*     *   *       * *",
    "******* *** ***** * *",
    "*       *   *     * *",
    "* ********* * ***** *",
    "*         * *       *",
    "* ******* * *********",
    "*       * *         *",
    "******* * ********* *",
    "*       *   *       *",
    "* ********* * ***** *",
    "*           *       *",
    "*********************"
]

# Define colors
wall_color = "blue"
food_color = "white"
pacman_color = "yellow"

# Create the maze grid
grid_size = 24
maze_width = len(maze[0]) * grid_size
maze_height = len(maze) * grid_size

# Create a dictionary to store turtle objects for each cell
maze_cells = {}

def create_maze():
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x = col * grid_size - maze_width / 2
            y = maze_height / 2 - row * grid_size

            if maze[row][col] == "*":
                maze_cells[(row, col)] = turtle.Turtle()
                maze_cells[(row, col)].speed(0)
                maze_cells[(row, col)].shape("square")
                maze_cells[(row, col)].color(wall_color)
                maze_cells[(row, col)].penup()
                maze_cells[(row, col)].goto(x, y)
                maze_cells[(row, col)].shapesize(grid_size / 20)

            if maze[row][col] == " ":
                maze_cells[(row, col)] = turtle.Turtle()
                maze_cells[(row, col)].speed(0)
                maze_cells[(row, col)].shape("circle")
                maze_cells[(row, col)].color(food_color)
                maze_cells[(row, col)].penup()
                maze_cells[(row, col)].goto(x, y)
                maze_cells[(row, col)].shapesize(0.5)

def create_pacman():
    pacman = turtle.Turtle()
    pacman.speed(0)
    pacman.shape("circle")
    pacman.color(pacman_color)
    pacman.penup()
    pacman.goto(0, 0)
    pacman.direction = "stop"

    return pacman

create_maze()
pacman = create_pacman()

# Main game loop
while True:
    # Update the screen
    screen.update()

    # TODO: Add game logic here

    # Exit the game loop
    break

# Exit the game
turtle.done()
