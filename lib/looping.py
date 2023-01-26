#!/usr/bin/env python3

def happy_new_year():
    for i in range(10):
        print(f"{10 - i}")
    print("Happy New Year!")

def square_integers(int_list):
    square_list = [number * number for number in int_list]
    return square_list

def fizzbuzz():
    for i in range(101):
        if i == 0:
            pass
        elif i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)

