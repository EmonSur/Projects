def index(my_list, value):
    '''
    -function to return the first index that value <occurs> in <list>
    :param list: - <my_list> input
    :param value: - <value> to search for
    :return:
    '''

    # use try/except to run code
    if type(my_list) == list: 
        # if my_list.count(value) == 0:
        #     return -1 
        # set counter
        i = 0
        # create an empty <list>
        list1 = []
        # loop over the length of <list>, ensuring <value> and the i'th value of <list> are not the same
        while i < len(my_list) and (my_list[i:i+1:] != [value]):
            # append i'th value to empty listmy_list[i:i+1:] != value)
            list1.append(my_list[i:i+1:])
            # increment the counter
            i += 1

        if list1.count(value) == 0:
            # to find the length <list> before <value> occurs. used to find the index <list>
            return i

    # set counter
    i = 0
    # create an empty <list>
    list2 = []
    str3 = str(value)
    str4 = str(my_list)
    # loop over the length of <list>, ensuring <value> and the i'th value of <list> are not the same
    while i < len(str4):
        # append i'th value to empty list
        list2.append(str4[i:i+1:])
        # increment the counter
        i += 1

    # set counter
    i = 0
    # create an empty <list>
    list2 = []
    str1 = str(value)
    str2 = str(my_list)
    # loop over the length of <list>, ensuring <value> and the i'th value of <list> are not the same
    while i < len(str2) and str2[i:i+1:] !=  str1:
        # append i'th value to empty list
        list2.append(str2[i:i+1:])
        # increment the counter
        i += 1

    if list2.count(value) == 0:
        # to find the length <list> before <value> occurs. used to find the index <list>
        return len(list2)

# print(index([1,2,3],3))


my_list = [1,2,3]
value = 1
# set counter
i = 0
# create an empty <list>
list2 = []
# loop over the length of <list>, ensuring <value> and the i'th value of <list> are not the same
while i < len(my_list):
    # append i'th value to empty listmy_list[i:i+1:] != value)
    list2.append(my_list[i:i+1:])
    # increment the counter
    i += 1

print(list2)


# if list2.count(value) == 0:
#     # to find the length <list> before <value> occurs. used to find the index <list>
#     return -1