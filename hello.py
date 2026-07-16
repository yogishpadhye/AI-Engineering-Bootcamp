
# in terminal, type code file_name.py to create a new python file
# in terminal, type python file_name.py to run the same file

""" Data type 1: str (string)"""

# name = input("What's your name? ")

# this is a comment because it started with '#'
"""
this is a comment open and closed in triple quotes
"""
# comma , separated arguments and adds a space before next argument
# + joins or concatenate the arguments inside print function
# + in furmula is addition

# print("Hello, ")
# print(name)
# print("Hello, " + name)

# print("Hello,", name)

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# *objects : print function can take infinite strings
# end='\n' : \n creates a new line; print function by default ends function with new line
# sep=' ' : multuple arguments are separate by space by default
# \ : backslash represents an escape character, whatever follows it is not considered as 'code' but rather treats it like a string

# print("Hello, ", end="")
# print(name)

# print(f"Hello, {name}")

# f"" is format function that formats everything inside it as defined

# strip() removes whitespaces before and after the str
# . is used to connect methods to strings
# name = name.strip()

# Capitalize user's name
# name = name.capitalize()

# title() capitalizes every word
# name = name.title()

# Lets join all methods together
# name = name.strip().title()

# take it to next level, add methods to input directly
name = input("What's your name? ").strip().title()

#print(f"Hello, {name}")

# split user's name into first and last name & call first name
first, last = name.split(" ")
print(f"Hello, {first}")


