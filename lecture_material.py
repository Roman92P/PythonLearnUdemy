print("hello world")

# Add line at the end according to standard PEP 8
# variable
# assignment
ex_var = 5

# reassignment
ex_var = 7

# vars without spaces, number at the begging
# no $!or ?
# camelCase
# snake_case
# numerAfter1stcChar

# Basic data types
float_1 = 1.234
int_1 = -7
bool_1 = True

int_2 = 1
float_2 = 2.1
bool_2 = False

int_2 = 4

# Math operators
# Expressions with addition, subtraction, division, multiplication + - / *
# exponentiation **
# floor division //
# modulo %

# Assignment operators =, +=
add_assign = 5
add_assign += 7

# -=, *=, /=, **=, %=

# Order
# () highest precedence
# **
# %,/,//,*
# + -

int_3 = 1 + 1
int_4 = 1 - 1
int_5 = 2 / 2
int_6 = 2 * 2
int_7 = 3 ** 8
int_8 = 10 // 3
int_9 = 17 % 5

print((4+5)*2)

# approximation errors that occur when using decimal numbers
print(1.23 + 2.80)

# The reason - Python was build on top of the C language (approximates floats using a fixed number of binary digits)

# First approach - use integers instead
print((123 + 280) / 100)

# Second approach - round()
print(round(1.23 + 2.80, 2))

print(round(16.68 + 6.98 + 16.78 + 15.26 + 3 + 4.39, 2))

# string data type. Sequence of characters
# single or double quotes are fine
ex_1 = 'This is a string'
ex_2 = "This is also a string"
# in a string each character has assigned index number
ex_7 = "0123456"
# use index to access index
print(ex_7[2])
print("apple"[0])

# string slicing
ex_8 = "tomato"
print(ex_8[:2])
print(ex_8[2:4])
print(ex_8[4:])

# concatenation
print("R2" + "-" + "D2")

# type() and str()
print(type(ex_8))
print(str(1.98))

# escape sequence
# \t tab indent
# \n new line
# \' or \"
# \\

# input()
# get input from the user
# name = input("Enter your name")
# print("Your name is " + name)

# turn strings into numbers
# int() and float()

# functions

# variables scope
# local scope - within the functions
# global scope

exampleScope = "asdasd"  # global scope


def loc_ex():
    exampleScope = "qwerty"  # local scope
    return exampleScope


# local variables cannot be used by code in the global scope
# global variables can be accessed by code in a local scope
# the local scope of one function can't use variables from another function's local scope
# use the same name for different variables as long as they are in different scopes

# global statement

def loc_ex1():
    global fruit
    fruit = "pear"
    print(fruit)


fruit = "apple"
loc_ex1()
print(fruit)

# flow control statements
# comparison operators: > < >= <=!= ==
# boolean operators and or not

# if statement
if True:
    print("True")

# else statement

if False:
    print("Do this")
else:
    print("Do else")

# elif statements

# Anything other than an empty string is truthy
# bool() function to get true or false for everything in ""

# while loops
counter = 0

while counter < 3:
    print("smth")
    counter += 1


# for loops

word = "house"

for letter in word:
    print(letter)

# range() is a function that returns the sequence of numbers
# and is usually used for iterating over with a  for loop

one_arg_input_range = range(5)

# from 0 to 4
# can be 3 arguments start, stop, step (can be negative)

# string methods are functions that are build into Python
# which allow you to perform useful operations with strings
# split change case
# upper(), lower()

print("lowtoUp".upper())
print("UPPERTOLOW".lower())

# isupper()
# islower()
# isalpha() true if only letters
# isalnum() if only numbers and letters
# isdecimal() only numbers
# isspace() is space
# istitle() only titlecase, all first latter capitalized
# startswith()
# endswith()
# join()
# split()
# .rjust() and .ljust(), can take one argument and return right or left justified version
# or second argument - what to use instead of spaces
# .center(), very similar to two above
# .strip(), .rstrip() and .lstrip() useful when you want to remove characters like spaces from the string
# .replace() takes two strings as an argument
# len() for string return the number of characters it contains
# .format(), placeholders with {}

# lists
# It is a data type which contains multiple values in an ordered sequence
# items
# could be different data types or another lists

example_list_1 = [5, 4, 3, 2, 1]

# list(), create list
# in and not in to check if item is in the list
checked_list = [1, 2]
print(1 in checked_list)

# indexes and slicing, list
# index start from zero
# we can access item by index "[]"
# negative index to retrieve from the end of the list [-1]
# Slicing, just like string slicing, e.g., [1:]
# Reassign is possible by accessing the item by index

# list methods
# del, to delete value from the list, by index
#  remove, remove what you passed as an argument from the list, the first from the list
# append() add argument to the end of the list
# insert(), add anywhere to the list
# sort() method to arrange items in the list, cannot be used on mixed type lists
# sort with reverse order (list.sort(reverse=True))
# sort - false is 0, true is 1
# sort uses ASCIIbetical order - uppercase letters come before lowercase letters
# fix this, key=str.lower
# .pop() remove and return the last item from the list. You can pass the index number

# lists are mutable vs strings are immutable
# deepcopy() allow you to create a copy of a list with its own reference when you need it.
# You need to import copy module.
# line continuation character \, but not for lists

# dictionaries are the data type which can store a collection of values like a list
# in dictionaries values are assigned to keys, which can be different data types
console = {"nintendo": "wii"}
# accesing items using keys
print(console["nintendo"])
# dictionaries are unordered
# are immutable
# copy - reference the same dictionary
# PEP8 allow each key in a new line
# you can check if a key exists in a dictionary wit in or not in
# dictionary methods .keys(), .values(), .items() (key and values retrieved at the same time(list of tuples)), .get()
# .fromkeys(), .pop()(you must use the key as an argument of pop), .popitem() (randomly chosen, not the last one)
ex_8 = {}.fromkeys(["address"], "Some address")  # created dictionary, 1 key
ex_9 = {}.fromkeys("address", "Some address")  # created dictionary, 7 keys
print(ex_8)
# without value, None will be set as a value for a key
# .clear()(removed everything and as a result empty dictionary), .copy(),
# .update() (add dictionary keys-value to another dictionary)
# .setdefault() give the values to keys that doesn't exist
console.setdefault("sony", "ps5")
# .dict(), an alternative way to create a dictionary
empty = dict()
not_empty = dict(a=1, b=2)

# tuples are the data type made up of a collection of items
# They  are enclosed in parentheses
tuple_1 = ("1", "b", 4)
tuple_2 = tuple("asdf")  # each char is item
# each item in the tuple has its index
# slicing the same way as strings and lists
# they are immutable, does not support item assignment
# take less space of memory
# you can have nested tuples
# count() how many appears item in the tuple
# index() will return the first item from the tuple

# sets is a data type that consists of a collection of items, much like a list.
# No duplicate
# Unordered
# can be different data types
set_1 = {9,8,7}  # set literal
set_2 = set({"a", "b", "c"})
# use range in set function range() with three arguments
# in can be used with sets to check for item in the set
# methods: add(), remove(), discard(), clear(), union(), intersection() (common element for two sets), difference()

# Set comprehension
comp_1 = {even+2 for even in range(2, 11, 2)}
print(comp_1)

comp_2 = {char.lower() for char in "Hello"}
print(comp_2)