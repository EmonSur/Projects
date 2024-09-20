# value = 1
# list = [2,9]
# min1 = min(list)
# print(len(list))
# print(ord(str(value)))

# print(ord(str(min1)))

# # def string_add_up(param2: str) -> int:

#     # i = 0
#     # if param[i] == 1:
#     #     ord1 = ord("1")
#         # return ord1

#     # i=0
#     # accum=0
#     # mn(min(param2))
#     # limit= len(param)
#     # while i < limit:
#     #     accum += ord(param[i])
#     #     i += 1

#     # return accum

#     # i = 0
#     # prm = param2[1]
#     # mn = min(param3)

    
#     # if ord(prm) < ord(mn):
#     #     param2 += param3
#     #     return param2

# print(ord("w"))


# param = [1,2]
# param2 = [3,4]
# print(ord(str(param[0])))



# # print(ord(index1))
# # prm = param2[1]
# # mn = min(param3)
# # ord1 = ord(prm)
# # ord2 = ord(mn)
# # print(mn)
# # print(ord(param2[i]))
# # print(ord(min(param3)))

# # print(string_add_up(param4))

# myval="55"
# # print(string_add_up(myval))

# # def test(param2,param3):

# #     min1 = min(param2)
     
# #     if ord(param2[1]) > ord(min1):
# #         return param2 + param3

# # param2 = [1,2]
# # param3 = [3,4]

# def add_to_list_no_sort(value,list=[]):
#     i = 0
#     min1 = min(list)
#     list_size = len(list)
#     if (list.count(value) == 0) and (ord(str(value)) < ord(str(min1))):
#         list.append(value)
#         while i < list_size:
#             list2.append(min1)
#             list.remove(min1)
#             i += 1
#     return list2

# value = 1
# list = ["a","b"]

#        # if (list.count(value) == 0) and (ord(str(value)) < ord(str(min1))):
#         #     list2.append(value)
#         #     while i < list_size:
#         #         list2.append(min1)
#         #         list.remove(min1)
#         #         i += 1
#         #     return list2
#         # if (list.count(value) == 0) and (ord(str(value)) > ord(str(min1))):
#         #     while i < list_size:
#         #         list2.append(min1)
#         #         list.remove(min1)
#         #         i += 1
#         #     list2.append(value)
#         #     return list2

#     # except:
#     #     try:
#     #         if (list.count(value) == 0) and (ord(str(value)) < ord(str(min1))):
#     #             list2.append(value)
#     #             while i < list_size:
#     #                 list2.append(min1)
#     #                 list.remove(min1)
#     #                 i += 1
#     #             return list2
#     #         if (list.count(value) == 0) and (ord(str(value)) > ord(str(min1))):
#     #             while i < list_size:
#     #                 list2.append(min1)
#     #                 list.remove(min1)
#     #                 i += 1
#     #             list2.append(value)
#     #             return list2
#     # # try:
#     #     list4 = []
#     #     list4.append(value)
#     #     i = 0
#     #     list5 = []
#     #     list_size = len(list)
#     #     if (list.count(value) == 0):
#     #     # and (type(value) == str):
#     #         while i < list_size:
#     #             min1 = min(list)
#     #             list5.append(min1)
#     #             list.remove(min1)
#     #             i += 1
#     #         list7 = list5 + list4
#     #         return list7
#     #     # elif (list.count(value) == 0) and (type(value) == int):
#     #     #     while i < list_size:
#     #     #         min1 = min(list)
#     #     #         list5.append(min1)
#     #     #         list.remove(min1)
#     #     #         i += 1
#     #     #     list6 = list4 + list5
#     #     #     return list6


#     # ''''''
def add_to_list_no_sort(value,list=[]):
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
    # if ord(str(value)) > ord(str(min1)):
    #     list2 = []
    #     i = 0
    #     list_size = len(list)
    #     while i < list_size:
    #         min1 = min(list)
    #         list2.append(min1)
    #         list.remove(min1)
    #         i += 1
    #     list2.append(value)
    #     return list2

# if ord(str(value)) < ord(str(min1)):
#     list2 = []
#     list2.append(value)
#     i = 0
#     list_size = len(list)
#     while i < list_size:
#         min1 = min(list)
#         list2.append(min1)
#         list.remove(min1)
#         i += 1
#     # list2.append(value)
#         return list2

print(add_to_list_no_sort(1,["w","e","q"]))
# value = 1
# min1 = 4
# print(ord(str(value)))
# print(ord(str(min1)))