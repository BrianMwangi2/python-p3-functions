#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

name = "Guido"

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")




# Method calls
greet_programmer()          # Output: Hello, programmer!
greet(name)                 # Output: Hello, Guido!
greet_with_default()        # Output: Hello, programmer!
greet_with_default(name)    # Output: Hello, Guido!


def add(num1, num2):
    return num1+num2
print(add(45,55))

def halve(number):
    return number/2
print(halve(100))
