# # alist = [5,6,7,8,9], [20,30,40]
# # alist = [1,2,3,4,5]
# alist = "hello world"
# i = 0 
# while i < len(alist):
#     print("index i:", i, " - value:", alist[i])
#     # here
#     j = 0 
#     while j < len(alist[i]):

#         inner_list = alist[i]
#         # print(inner_list)

#         # print("index j:", j, " - value:", inner_list[j])
#         print("index j:", j, " - value:", alist[i][j])
#         # print("index j:", j, " - value:", "hello"[j])
#         # print("index j:", j, " - value:", "h")
#         j += 1

    # to here
    # i += 1

def tester(param1):
    var =""
    i=0
    while i <len(param1):
        var += str(param1[i])
        i += 1
    return var

alist1 = "hello world"
# alist1 = ["h", "i", " ", "t", "h", "e", "r", "e"]
alist2 = [1,6,7,8,9]
# print(tester(alist1))
print(tester(alist2))