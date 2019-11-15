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
a = 12
b = 3
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

c = a + b
d = c / 3
e = d - 4
print(e * 12)

parrot = "Norwegian Blue"
print(parrot)
print(parrot[0])  # This syntax will print the specified index
print(parrot[3])
print(parrot[-1])
# This syntax tells where to start printing and how many characters to print from the starting index. In this case it will print 6 total characters starting from index 0. Print everything from index 0 up to, but not including index 6.
print(parrot[0:6])
print(parrot[:6])  # Prints from 0 up to but not including 6.
print(parrot[6:])  # Prints from 6 to the end of the string.
print(parrot[-4:-2])  # Prints Bl in this case.
# Start an index zero and print everything up to but not including index six in steps of two. This will print every other letter.
print(parrot[0:6:2])
# Start an index zero and print everything up to but not including index six in steps of three. This will print every two letters.
print(parrot[0:6:3])

# Two colons will print everything in a string starting at the index of the first number in steps defined by the second one. This can be useful for extracting specific information in a pattern.
random_numbers = "9,223,372,036,854,775,807"
print(random_numbers[1::4])
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])

# String operators
string1 = "He's "
string2 = "probably "
string3 = "pining"
print(string1 + string2 + string3)

# When using a string literal instead of variables, you don't need to use the plus sign operator. While this does work, it's not exactly practical.
print("He's " "probably " "pining")

# Multiplication of strings
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "thursday"
print("day" in today)
print("thurs" in today)
print("fri" in today)
print("parrot" in "fjord")
