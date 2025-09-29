
# define a function that will return the square a number that's given.
def square(number):
    square = number ** 2
    return f"{number} squared is {square}"

# define a function that will return whether a number is odd or even.
def OddOrEven(number):

    # If number has no remainder when divided by 2, attribute even to result variable.
    if number % 2 == 0:
        result = "even"

    # Or else, attribute odd to result variable.
    else:
        result = "odd"
    return f"{number} is an {result} number"

# Define a function that takes a list of numbers and finds the average.
def Average(numbers):

    # Set the toal to zero and then add each number in the list to the total.
    total = 0
    for number in numbers:
        total += number

    # Find the average and round it to one decimal place.
    average = float(total / len(numbers))
    average = f"{average:.1f}"


    return f"Average is {average}"


