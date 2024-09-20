# ScriptName: my_functions.py
# Author: Emon Monsur 121367643

# template for calling functions in another file 

print(ord(str(5)))

def print_function():
    print("I'm in another file :)")

def seasons(number):
    '''
    seasons - function to give the number inputed by the user a corresponding season value    
    :number - integer value  
    list used here; taking the users input value, and using the users input -1 to get the index value for the corresponding season in the list  
    give an error value if a int outside range or a non int value is given
    '''
    input = ["Winter","Spring","Summer","Autumn"]
    try:
        if number > 0 and number < 5:
            return input[number-1]
        if number > 4 or number < 0:
            return "Number entered "+str(number)+" is outside of input values"
    except:
        return "Input value must be a number"

def slice_reverse(input_value):
    '''
    To determine if the input_value is a palindrome i.e. reads the same backwards as forwards. 
    The program should return True or False(booleans) depending on the input.
    - reverse() function cannot be used
    '''

    i = 0
    input_list = []
    while i < len(input_value):
        input_list.extend(list(str(input_value[i])))
        i += 1
    if input_list == input_list[::-1]:
        return True
    if input_list != input_list[::-1]:
        return False

def add_to_list(value,list=[]):
    '''
    Function that will return a sorted list.   
    This function will add value to the list if the list does not already contain the value.
    Value will be returned of no list is given '''
    str(list)
    try:
        if type(list)== str or type(list)== int or type(list)== float or type(list)== tuple:
            return "Incorrect value defined for paramlist"
        if list == []:
            return [value]
        if value in list:
            list.sort()
            return list
        if list.count(value) == 0:
            list.append(value)
            list.sort()
            return list
    except:
        return "sort() does not like this mixture of elements"

def add_to_list_no_sort(value,list=[]):

    '''
    Function that'll return a sorted list.   
    This function will work the way as add_to_list, adding value to the list if the list does not already contain the value.
    - sort() will not be able to be used though.
    ASCII values may be a solution'''

    try:
        if list == []:
            return [value]
        if type(value) != str and type(value) != int and type(value) != float:
            return "Incorrect type of value inputted to be added into param list"
        if value in list:
            i = 0
            list2 = []
            list_size = len(list)       
            while i < list_size:
                min1 = min(list)
                list2.append(min1)
                list.remove(min1)
                i += 1
            return list2
        else:
            i = 0
            list2 = []
            list.append(str(value))
            list_size = len(list)
            while i < list_size:
                min1 = min(list)
                list2.append(min1)
                list.remove(min1)
                i += 1
            return list2
    except:
        return "Incorrect value defined for param list"