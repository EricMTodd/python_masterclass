# print("sup nerd")

# greeting = "Hello"
# name = input("Please enter your name: ")

# print(f'{greeting} {name}')


# The following are ways to modify terminal output

# \n after a string will print everything after it on a new line
splitString = ("This string\nhas been\nsplit over\nseveral lines")
print(splitString)

# \t after a string will input a tabbed space
tabbedString = "1\t2\t3\t4\t5\t"
print(tabbedString)

# These are methods for including multiple quotation marks when printing strings.
print('The pet shop owner said "No, no, he\'s uh... He\'s resting"')
print("The pet shop owner said \"No, no, he's uh... He's resting\"")

# Triple quotes are a method of splitting strings onto new lines easily as well as including multiple kinds of quotatin marks within the string to be printed.
anotherSplitString = """This string
has been
split over
several lines"""

print(anotherSplitString)

print("""The pet shop ownder said "No, no, he's uh... He's resting." """)
print('''The pet shop ownder said "No, no, he's uh... He's resting." ''')
