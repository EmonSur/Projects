# def add_to_list_no_sort(value,list=[]):

#     if list == []:
#         return [value]
#     if value in list:
#         i = 0
#         list2 = []
#         list_size = len(list)
#         while i < list_size:
#             min1 = min(list)
#             list2.append(min1)
#             list.remove(min1)
#             i += 1
#         return list2
#     # if list.count(value) == 0:
#     #     list.append(value)
#     #     list2 = []
#     #     i = 0
#     #     list_size = len(list)
#     #     while i < list_size:
#     #         min1 = min(list)
#     #         list2.append(min1)
#     #         list.remove(min1)
#     #         i += 1
#     #     return list2
#     min1 = min(list)
#     if ord(str(value)) < ord(str(min1)):
#         list2 = []
#         list2.append(value)
#         i = 0
#         list_size = len(list)
#         while i < list_size:
#             min1 = min(list)
#             list2.append(min1)
#             list.remove(min1)
#             i += 1
#         return list2
#     min1 = min(list)
#     if ord(str(value)) > ord(str(min1)):
#         list2 = []
#         i = 0
#         list_size = len(list)
#         while i < list_size:
#             min1 = min(list)
#             list2.append(min1)
#             list.remove(min1)
#             i += 1
#         list2.append(value)
#         return list2

def add_to_list_no_sort(value,list=[]):

    try:
        if list == []:
            return [value]
        i = 0
        list2 = []
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
        min1 = min(list)
        if ord(str(value)) < ord(str(min1)):
            list2 = []
            list2.append(value)
            i = 0
            list_size = len(list)
            while i < list_size:
                min1 = min(list)
                list2.append(min1)
                list.remove(min1)
                i += 1
            return list2
        min1 = min(list)
        if (list.count(value) == 0) and (ord(str(value)) > ord(str(min1))):
            i = 0
            list2 = []
            list_size = len(list)
            while i < list_size:
                min1 = min(list)
                list2.append(min1)
                list.remove(min1)
                i += 1
            list2.append(value)
            return list2
        if list.count(value) == 0:
            i = 0
            list2 = []
            list.append(value)
            list_size = len(list)
            while i < list_size:
                min1 = min(list)
                list2.append(min1)
                list.remove(min1)
                i += 1
            return list2
    except:
        return "Incorrect value defined for paramlist"

print(add_to_list_no_sort(5))