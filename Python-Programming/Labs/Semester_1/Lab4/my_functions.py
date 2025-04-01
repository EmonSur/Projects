# ScriptName: my_functions.py
# Author: Emon Monsur 121367643

# template for calling functions in another file
import math

def print_function():
   print("I'm in another file :)")


def seperated_input(param1, param2, sepr="", endr="/n"):
    '''
    param1 - string value
    param2 - string value
    sepr - sep string value
    endr - end string value
    '''

    print(str.capitalize(param1),sepr, str.capitalize(param2),endr)


def three_numbers(number_1, number_2, number_3):
    '''
    
    
    '''

    if number_1 == number_2 == number_3:

        return True

    elif number_1 != number_2 != number_3:

        return False


def seasons(number):
    '''
    
    '''
    if type(number) != int :
        return ("Input value must be a number")
    if number == 1:
        return ("Winter")
    elif number == 2:
        return "Spring"

    elif number == 3:
        return "Summer"

    elif number == 4:
        return "Autumn"

    elif number >= 4 or number < 1:
        return "Number entered, " + str(number) + ", is outside of input values"
    if type(number) == str :
        return ("Input value must be a number")

    else:
        return

    

def grades(percent):

    if type(percent) != int:
        return "Input value must be a number"
    
    if percent >= 85 and percent <= 100:
        return "A"
        
    if percent >= 70 and percent <= 84:
        return "B"

    if percent >= 55 and percent <= 69:
        return "C"

    if percent >= 40 and percent <= 54:
        return "D"

    if percent >= 25 and percent <= 39:
        return "E"

    if percent >= 0 and percent <= 24:
        return "F"

    if percent >= 100 or percent <= 0:
        return "X"
    else:
        return

    
def equal_numbers(number1,number2):

    if type(number1) != int or type(number2) != int:
        return "Input value(s) must be a number"


    if number1 == number2:
        return math.sqrt(number1)  

    if number1 != number2:
        return (number1 ** 2,number2 ** 2)

    else:
        return

    
    
