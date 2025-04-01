# ScriptName: my_functions.py
# Author: Emon Monsur 121367643

# template for calling functions in another file


def print_function():
    print("I'm in another file :)")


def count(my_list, value):
    '''
    function - count how many times <value> occurs in <my_list>
    :param list: - <my_list> input
    :param value: - <value> to search for
    :return:
    '''
    try:
        if (type(my_list) == int and type(value) == int) or (type(my_list) == float and type(value) == float):
            my_list = str(my_list)
            value = str(value)
        if my_list.count(value) == 0:
            return "Houston, we have a problem!"
        i = 0
        num_values = 0
        while i < len(my_list):
            if my_list[i] == value:
                num_values += 1
            i += 1
        return num_values   
    except:
        "Houston, we have a problem!"

def index(my_list, value):
    '''
    -function to return the first index that value <occurs> in <list>
    :param list: - <my_list> input
    :param value: - <value> to search for
    :return:
    '''
    try: 

        if type(my_list) == list: 
            if my_list.count(value) == 0:
                return -1
            i = 0
            list1 = []
            while i < len(my_list) and (my_list[i:i+1:] != [value]):
                list1.append(my_list[i:i+1:])
                i += 1

            if list1.count(value) == 0:
                return len(list1)

        i = 0
        list1 = []
        str1 = str(value)
        str2 = str(my_list)


        while i < len(str2):
            list1.append(str2[i:i+1:])
            i += 1

        if list1.count(value) == 0:
            return -1

        i = 0
        list2 = []
        str1 = str(value)
        str2 = str(my_list)
        while i < len(str2) and str2[i:i+1:] !=  str1:
            list2.append(str2[i:i+1:])
            i += 1

        if list2.count(value) == 0:
            return len(list2)
    except:
        "Houston, we have a problem!"   

def get_value(my_list,index):
    '''
    -function to return the <value> that occurs in <list> at index
    :param list: - <my_list> input
    :param value: - index in which a <value> occurs
    :return:
    '''
    try:
        if type(index) != int:
            return "Houston, we have a problem!" 
        if len(my_list) < index + 1 or len(my_list) > index + 1:
            return "Houston, we have a problem!" 
        if type(my_list) == int or type(my_list) == float:
            my_list = str(my_list)
        if len(my_list) >= (index + 1):
            return my_list[index]
    except:
        "Houston, we have a problem!"            

def insert(my_list,index, value):
    '''
    -function to return my_list, after you have added value at index 
    (remember to check the length of my_list and if index is larger than len(my_list) add as a new index at the end my_list)
    :param list: - <my_list> input
    :param index: - <index> input
    :param value: - <value> that is added at index of <my_list>
    :return:
    '''
    try:
        if type(my_list) == list or type(my_list) == tuple:
            return "Houston, we have a problem!"
        if type(my_list) == int or type(my_list) == float:
            my_list = str(my_list)
        if len(my_list) < (index + 1):
            i = 0
            list1 = []
            while i < len(my_list):
                list1.append(my_list[i])
                i += 1
            list1.append(value)

            if type(my_list) == list or type(my_list) == tuple:
                return list1

            i = 0 
            val1 = ""
            while i < len(my_list):
                val1 += str(my_list[i])
                i += 1
            val1 += str(value)
            return val1

        i = 0
        list2 = []
        while i < index:
            list2.append(my_list[i])
            i += 1
        list2.append(value)

        while i < len(my_list) - 1:
            i += 1
            list2.append(my_list[i])

        if type(my_list) == list:
            return list2

        if len(my_list) >= (index + 1):
            i = 0 
            list3 = ""
            while i < len(list2):
                list3 += str(list2[i])
                i += 1
            return list3
    except:
        "Houston, we have a problem!"            
        


def value_in_list(my_list, value):
    '''
    -function to return True or False if value occurs in my_list
    :param list: - <my_list> input
    :param value: - <value> that is tested to see if occurs in <my_list>
    :return:
    '''

    try:
        if type(my_list) == int or type(my_list) == float:
            my_list = str(my_list)
        if type(value) == int or type(value) == float:
            value = str(value)
        i = 0
        list1 = []
        while i < len(my_list):
            list1.append(my_list[i])
            i += 1

        if list1.count(value) == 0:
            return False
        if list1.count(value) != 0:
            return True
    except:
        "Houston, we have a problem!"

def concat(list1, list2):
    '''
    -function to return a new list, which is a combination of list1 and list2i.
    :param list: - <list1> input
    :param list: - <list2> input
    :return:
    '''

    try:
        if type(list1) == type(list2):
            return "Houston, we have a problem!"
        if type(list1) == list and type(list2) != list:
            return list1.append(list2)
        if type(list1) == int or type(list1) == float:
            list1 = str(list1)
        if type(list2) == int or type(list2) == float:
            list2 = str(list2)

        i = 0
        my_list = []
        while i < len(list1):
            my_list.append(list1[i])
            i += 1

        i = 0
        while i < len(list2):
            my_list.append(list2[i])
            i += 1

        if type(list1) == list and type(list2) == list:
            return my_list

        i = 0 
        str1 = ""
        while i < len(my_list):
            str1 += my_list[i]
            i += 1

        if len(str1) != 0:
            return str1
    except:
        "Houston, we have a problem!"

def remove(value, my_list):
    '''
    -function to return a list with the first occurrence of value removed from my_list
    :param value: - <value> that is removed from <my_list>
    :param list: - <my_list> input
    :return:
    '''

    try:
        if type(my_list) == list or type(my_list) == tuple:
            return "Houston, we have a problem!"
        if my_list.count(value) != 0:
            list1 = []
            i = 0
            while i < len(my_list) and my_list[i] != value:
                list1.append(my_list[i])
                i += 1
            return list1
        if type(my_list) == int or type(my_list) == float:
            my_list = str(my_list)
        if type(value) == int or type(value) == float:
            value = str(value)

        i = 0
        list1 = []
        while i < len(my_list) and (ord(str(value)) != ord(str(my_list[i]))):
            list1.append(my_list[i])
            i += 1
        i += 1

        while i < len(my_list):
            list1.append(my_list[i])
            i += 1

        if type(my_list) == list:
            return list1

        if list1.count(value) == 0:
            i = 0 
            list2 = ""
            while i < len(list1):
                list2 += str(list1[i])
                i += 1
            return list2

    except:
        "Houston, we have a problem!"








    

