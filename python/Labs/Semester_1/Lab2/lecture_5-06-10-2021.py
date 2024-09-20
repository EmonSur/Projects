#Script Name: Function Sample Code
#Author: Emon Monsur 121367643
'''
# averge ages:
# get the first age
age1 = int(input("Please enter age 1: "))
# get the second age
age2 = int(input("Please enter age 2: "))
# determine the average age
average = (age1+age2)/2
# print to screen
print("The average age is %d" % average)
'''

'''
# averge ages - remove the strings from input()
# and create seperate variables for the strings
# get the first age
input_string_1 = "Please enter age 1: "
age1 = int(input(input_string_1))
# get the second age
input_string_2 = "Please enter age 2: "
age2 = int(input(input_string_2))
# determine the average age
average = (age1+age2)/2
# print to screen
print("The average age is %d" % average)


'''
'''
def ask_for_int_input(question_string):
# save the input from the user in a variable called "user_input"
      userinput = int(input(question_string))
# get the first age
input_string_1 = "Please enter age 1: "
age1 = int(input(input_string_1))
# get the second age
input_string_2 = "Please enter age 2: "
age2 = int(input(input_string_2))
# determine the average age
average = (age1+age2)/2
# print to screen
print("The average age is %d" % average)
'''



''' a function that returns an integer value from the user '''

'''
def ask_for_int_input(question_string):
    # save the input from the user in a variable called "user_input"
    user_input = int(input(question_string))
    # return the content of the variable called "user_input"
    return user_input


age1 = ask_for_int_input("Please enter age 1: ")
# get the second age
age2 = ask_for_int_input("Please enter age 2: ")
# determine the average age
average = (age1+age2)/2
# print to screen
print("The average age is %d" % average)
'''

'''
# function to return an int value from the user


def ask_for_int_input(question_string):
    # save the input from the user in a variable called "user_input"
    user_input = int(input(question_string))
    # return the content of the variable called "user_input"
    return user_input


# get the first age
input_string_1 = "Please enter age 1: "
age1 = ask_for_int_input(input_string_1)
print(id(age1))
# get the second age
input_string_2 = "Please enter age 2: "
age2 = ask_for_int_input(input_string_2)
print(id(age2))
# determine the average age
average = (age1+age2)/2
# print to screen
print("The average age is %d" % average)
'''

'''
def ask_for_int_input(question_string):
    print("The id for question_string with a value of",
          question_string, "is", id(question_string))
    # save the input from the user in a variable called "user_input"
    user_input = int(input(question_string))
    print("The id for user_input with a value of",
          user_input, "is", id(user_input))
    # return the content of the variable called "user_input"
    return user_input


# get the first age
input_string_1 = "Please enter age 1: "
print("The id for input_string_1 with a value of",
      input_string_1, "is", id(input_string_1))
age1 = ask_for_int_input(input_string_1)
print("The id for age1 with a value of",
      age1, "is", id(age1))
# get the second age
input_string_2 = "Please enter age 2: "
print("The id for input_string_2 with a value of",
      input_string_2, "is", id(input_string_2))
age2 = ask_for_int_input(input_string_2)
print("The id for age2 with a value of",
      age2, "is", id(age2))
# determine the average age
average = (age1+age2)/2
# print to screen
print("The average age is %d" % average)
'''