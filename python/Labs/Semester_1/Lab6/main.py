# ScriptName: main.py
# Author: Emon Monsur 121367643

# template for calling functions in another file

# import my_functions from other files - different options
# from my_functions import print_function
# import my_functions - when you use this you need to call the function using 'my_functions.<function_name>'
# this option imports all my_functions, using '*'
from my_functions import *

def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()



if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()
    
    print(seasons(-1))
    print(slice_reverse([1,2,3,2,1]))
    print(slice_reverse(["a", "b", "c", "d"]))
    print(slice_reverse([1, 2, 3, 4]))
    print(slice_reverse(["a", "b", "a"]))
    print(slice_reverse([12321]))
    print(slice_reverse([12345]))
    print(slice_reverse([123,44,321]))
    print(slice_reverse(["ab", "ba"]))
    print(slice_reverse(["abc", 1232, 1, "cba"]))
    print(slice_reverse(["abc", 123, 55]))
    print(add_to_list_no_sort(0,[1,2]))
    print(add_to_list_no_sort("w"))

    print(add_to_list(5, [1,3,7,9]))
    print(add_to_list("c", ["a","b","d","e"]))
    print(add_to_list(5, [1,5,7,9]))
    print(add_to_list(5))
    print(add_to_list(5, 5))
    print(add_to_list(5, ["a","d","e"]))

    print(add_to_list_no_sort(5, [1,3,7,9]))
    print(add_to_list_no_sort("c", ["a","b","d","e"]))
    print(add_to_list_no_sort(5, [1,5,7,9]))
    print(add_to_list_no_sort(5))
    print(add_to_list_no_sort(5, 5))
    print(add_to_list_no_sort(5, ["a","d","e"]))