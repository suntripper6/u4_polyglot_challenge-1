from decimal import *  # SOURCE: https://docs.python.org/3/library/decimal.html

# Challenge 1:  add_List

# Prompt:
# - Write a function called add_list that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
# - If called with no arguments, return 0 (zero).
# - If any non-number arguments are in the argument, return "NaN"


# Examples:
# add(1) //=> 1
# add(1,50,1.23) //=> 52.23
# add(7,-12) //=> -5
# add("peanut_butter", "marshmellow_fluff") //=> NaN

# -----------------------------------------------
# Solution Goes Here - >
# -----------------------------------------------
def add_list(*args):
    sum = 0
    if args == 0:
        return 0

    for num in args:
        sum += num

    return sum


# print(add_list(1, 3, 24))


# Challenge 2: remove_ends

# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

# -----------------------------------------------
# Solution Goes Here - >
# -----------------------------------------------
def remove_ends(str):
    if len(str) < 3:
        return ""

    result = ""
    result = str[1:-1]

    return result


# print(remove_ends("a"))

# Challenge 3: is_palindrome

# Prompt:
# - Write a function called is_palindrome that accepts a single string argument, then returns true or false depending upon whether or not the string is a palindrome.
# - A palindrome is a word or phrase that is the same forward or backward.
# - Casing and spaces are not included when considering whether or not a string is a palindrome.
# - If the length of the string is 0 or 1, return true.
# Examples:
# is_palindrome('SEI Rocks'); //=> false
# is_palindrome('rotor'); //=> true
# is_palindrome('A nut for a jar of tuna'); //=> true
# is_palindrome(''); //=> true

# -----------------------------------------------
# Solution Goes Here - >
# -----------------------------------------------


def is_palindrome(str):
    if len(str) == 0 or len(str) == 1:
        return True

    formated_input = str.lower().replace(" ", "")

    if formated_input == formated_input[::-1]:
        return True
    else:
        return False


# print(is_palindrome("A nut for a jar of tuna"))


# Challenge 4: is_prime

# Prompt:
# - Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
# Examples:
# is_prime(2) //=> true
# is_prime(3) //=> true
# is_prime(4) //=> false
# is_prime(29) //=> true
# is_prime(200) //=> false

# -----------------------------------------------
# Solution goes here ->
# -----------------------------------------------

def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True
    return False


# print(is_prime(200))

# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost if there is an 8.5% sales tax attached to each item.
# Then set up a conditional that adds a $10 Shipping Fee if the user lives in HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL.
# All other states recieve free shipping.

# Your function should take the list and the user's homestate as arguments

shopping_cart = [
    {"item": "headphones", "price": 25},
    {"item": "speakers", "price": 40},
    {"item": "microphone", "price": 70},
    {"item": "lamp", "price": 15},
    {"item": "tower fan", "price": 35},
]

# for prices in shopping_cart:
#     print(prices.get("price"))

# -----------------------------------------------
# Solution Goes Here ->
# -----------------------------------------------


def total_checkout_cost(dictionary, home_state):
    cost = 0
    tax = .085
    cost_per_item = []

    ten_dollars = ["HI", "AK", "TX", "FL"]
    five_dollars = ["AL", "MS", "NV", "IL"]

    for items in dictionary:
        cost = round(items.get("price") + Decimal(items.get("price") * tax), 2)
        item = items.get("item")
        if home_state in ten_dollars:
            cost += 10
            cost_per_item.append(
                f"Home State: {home_state} Item: {item} Total Price: {cost}")
        elif home_state in five_dollars:
            cost += 5
            cost_per_item.append(
                f"Home State: {home_state} Item: {item} Total Price: {cost}")
        else:
            cost_per_item.append(
                f"Home State: {home_state} Item: {item} Total Price: {cost}")

    return cost_per_item


# print(total_checkout_cost(shopping_cart, "FL"))
# print(total_checkout_cost(shopping_cart, "AL"))
# print(total_checkout_cost(shopping_cart, "NY"))


# Challenge 6: fizz_buzz
# Prompt -> Write a program that prints the numbers from 1 to 50. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”
# If your argument is not a number, return "is not a number"

# Examples:
# fizz_buzz(10) //=> 10 "Buzz"
# fizz_buzz(30) //=> 30 "FizzBuzz"
# fizz_buzz(18) //=> 18 "Fizz"
# fizz_buzz(22) //=> 22 ""
# fizz_buzz(ham_sandwich) //=> "ham_sandwich is not a Number"
# -----------------------------------------------
# Solution Goes Here ->


def fizz_buzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


# print(fizz_buzz())

# -----------------------------------------------
# Challenge 7 - Chessboard Creator
# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).
# Making a digital chessboard is an interesting way of visualising how loops can work together.
# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.
# So chess_board(6,4) should return an array like this:
[
    ["O", "X", "O", "X"],
    ["X", "O", "X", "O"],
    ["O", "X", "O", "X"],
    ["X", "O", "X", "O"],
    ["O", "X", "O", "X"],
    ["X", "O", "X", "O"]
]
# And chess_board(3,7) should return this:


[
    ["O", "X", "O", "X", "O", "X", "O"],
    ["X", "O", "X", "O", "X", "O", "X"],
    ["O", "X", "O", "X", "O", "X", "O"]
]

# The white spaces should be represented by an: 'O' and the black an: 'X'

# The first row should always start with a white space 'O'


# -----------------------------------------------
# Solution Goes Here - >
# -----------------------------------------------
def chess_board(row, column):
    board = []
    for r in range(row):
        row = []
        for c in range(column):
            if (r + c) % 2 == 0:
                row.append("O")
            else:
                row.append("X")
        board.append(row)

    for row in board:
        print(row)


# print(chess_board(8, 8))
