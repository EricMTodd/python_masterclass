# print("sup nerd")

# greeting = "Hello"
# name = input("Please enter your name: ")

# print(f'{greeting} {name}')


# The following are ways to modify terminal output

# # \n after a string will print everything after it on a new line
# splitString = ("This string\nhas been\nsplit over\nseveral lines")
# print(splitString)
# print()

# # \t after a string will input a tabbed space
# tabbedString = "1\t2\t3\t4\t5\t"
# print(tabbedString)
# print()

# # These are methods for including multiple quotation marks when printing strings.
# print('The pet shop owner said "No, no, he\'s uh... He\'s resting"')
# print("The pet shop owner said \"No, no, he's uh... He's resting\"")
# print()

# # Triple quotes are a method of splitting strings onto new lines easily as well as including multiple kinds of quotatin marks within the string to be printed.
# anotherSplitString = """This string
# has been
# split over
# several lines"""

# print(anotherSplitString)
# print()

# print("""The pet shop ownder said "No, no, he's uh... He's resting." """)
# print('''The pet shop ownder said "No, no, he's uh... He's resting." ''')
# print()


# # Variable names must always start with either a letter or an underscore.

# # Truthy
# greeting = "Bruce"
# _myName = "Eric"
# Eric93 = "Good"
# Eric_Was_25 = "Hello"
# Greeting = "There"

# # Falsey
# # 1Eric = "Bad"

# print(Eric_Was_25 + ' ' + greeting)

# age = 24
# print(age)

# print(greeting + age)

# # An expression is anything that can be calculated to return a value.
# # Numeric and sequence types
# # Strings are sequence types
# # Integers are whole numbers
# # Floats are decimal or fractional numbers
# a = 12
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)  # This returns a float
# print(a // b)  # This returns a whole number
# print(a % b)

# # This will return the numbers 0 - 3
# for i in range(1, 4):
#     print(i)

# # This will throw an error because it is trying to loop through the range using a float, which python cannot do.
# for i in range(1, a/b):
#     print(i)

# # This will return the numbers 0 - 3 because the operation returns the whole number value of four, which is equivalent to the first loop.
# for i in range(1, a//b):
#     print(i)


# # Remember that operator precedence, or order of operations is always evaluated in Python.
# print(a + b / 3 - 4 * 12)  # Evaluates to -35.0
# print(8 / 2 * 3)  # Evaluates to 12.0
# print(8 * 3 / 2)  # Evaluates to 12.0

# # Use brackets just like you would in mathematics to modify operator precedence.
# # This is a similar operation to the first one, but instead evaluates to 12.0
# print((((a + b) / 3) - 4) * 12)

# # Challenge successfully passed on the first try!
# bun_price = 2.40
# money = 15
# total_buns = money // bun_price
# print(total_buns)
