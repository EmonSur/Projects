# ScriptName: my_functions.py
# Author: Emon Monsur 121367643

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")

def fizz_buzz(num1,divisor_1 = 3,divisor_2 = 5):

    if type(num1) != int or type(divisor_1) != int or type(divisor_2) != int:
        return "Input value(s) must be a number"
    if num1 % divisor_1 == 0 and num1 % divisor_2 == 0:
        return "FizzBuzz"
    if num1 % divisor_1 == 0:
        return "Fizz"
    if num1 % divisor_2 == 0:
        return "Buzz"
    if num1 % divisor_1 != 0 or num1 % divisor_2 != 0:
        return num1
    else:
        return

def grades(number):

    if type(number) != int and type(number) != str:
        return "Input value must be a number or a letter"
    if number == "A":
        return "85-100"
    if number == "B":
        return "70-84"
    if number == "C":
        return "55-74"
    if number == "D":
        return "40-54"
    if number == "E":
        return "25-39"
    if number == "F":
        return "0-24"
    if type(number) == str:
        return "The input letter grade is outside the range supported"
    if number >= 85 and number <= 100:
        return "A"        
    if number >= 70 and number <= 84:
        return "B"
    if number >= 55 and number <= 69:
        return "C"
    if number >= 40 and number <= 54:
        return "D"
    if number >= 25 and number <= 39:
        return "E"
    if number >= 0 and number <= 24:
        return "F"
    if number > 100 or number < 0:
        return "The input numerical grade is outside the range supported"
    else:
        return

    
