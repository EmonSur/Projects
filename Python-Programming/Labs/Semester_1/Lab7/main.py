# ScriptName: main.py
# Author: Jason Quinlan

# template for calling functions in another file

# import functions from other files - different options
# from functions import print_function
# import functions - when you use this you need to call the function using 'functions.<function_name>'
# this option imports all functions, using '*'
from my_functions import *


def main():
    """
    Call the functions defined in the functions.py file
    """
    print_function()

    # test count
    # print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], "a"))
    # print(count([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1], 8))
    # print(count("hello", "l"))
    # print(count("hello", "h"))
    # print(count(123,2))

    # print(index("hello",5)) 
    # print(get_value("hello", 5)) 
    print(insert(("h","e","l","l","O"), 99, "p"))
    # print(value_in_list(123,2))
    # print(concat([1,2,3],4))
    # print(remove("l",("w","E",)))


if __name__ == "__main__":
    ''' call the main() function in this file '''
    main()

