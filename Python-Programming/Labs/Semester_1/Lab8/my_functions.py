# ScriptName: my_functions.py
# Author: Emon Monsur 121367643

import random

def print_function():
    print("I'm in another file :)")

def is_stairs( s = [] ):
    '''
    -function to check if a list is a stairs
    . A stairs is a list of at least two numbers where either:
    i. each number is one greater than the previous number or
    ii. each number is one smaller than the previous number
    iii. but always going in the one direction – always up or always down.
    :param list: - <s> input
    :return:
    '''

    try:
        if type(s) != list:
            return "How can I get the second floor if I do not have stairs?"
        
        if len(s) == 1 or s == []:
            return False
        
        for val in s:
            val = str(val)
            if len(val) > 1:
                return "How can I get the second floor if I do not have stairs?"
            
        for val in s:
            index1 = s.index(val)
            if type(val) == type(s[index1 + 1]):
                return "How can I get the second floor if I do not have stairs?"
        
        # if <value(s)> of s type <str>, convert <value(s)> into their ascii values
        if type(s[0]) == str:
            s2 = []
            for val in s:
                s2.append(val.lower())
            s = [ord(val2) for val1 in s2 for val2 in val1]
        
        if type(s[0]) != str:
            # create a <list> of 1 greater than all the <value(s)> of s
            s2 = s

        # check if the 1st <value> is smaller than the 2nd <value>. if so <list> is ascending
        if s2[0] < s2[1]:
            for val in s2:
                index1 = s2.index(val)
                if index1 == len(s2) - 1:
                    break
                ans = ""
                if val + 1 == s2[index1 + 1]:
                    ans = True        

            if ans == True:
                return True
            else:
                return False
        
        # this is repeated with little changes to see if s is a <list> where each number is one smaller than the previous number
        if s2[0] > s2[1]:
            for val in s2:
                index1 = s2.index(val)
                if index1 == len(s2) - 1:
                    break
                ans = ""
                if val - 1 == s2[index1 + 1]:
                    ans = True

            if ans == True:
                return True
            else:
                return False
            
        if s2[0] == s2[1]:
            return False
    except:
        return "How can I get the second floor if I do not have stairs?"


def while_loop(max_number=[]):
    '''
    -function containing a while loop that loops from 1 to n, where n is a
    positive number, saving the number in a list on each loop.
    The function shall return the list of all numbers.
    :param value> <value> till which the loop will continue
    :return:
    '''
    try:
        if max_number == []:
            return "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 55]"
        
        if max_number != [] and type(max_number) != int:
            return "Did you break the break or should we continue?"
        
        if max_number == 0:
            return "[0, 0]"
        
        if max_number > 0:
            max_list = []

            if max_number > 12:
                max_number = 12

            i = 1
            while i <= max_number:
                max_list.append(i)
                i += 1
                
            total = 0

            for val in max_list:
                total += val

            max_list.append(total)

            return max_list

        if max_number < 0:
            min_list = []

            if max_number < -12:
                max_number = -12

            i = -1
            while i >= max_number:
                min_list.append(i)
                i -= 1

            total = 0

            for val in min_list:
                total += val

            min_list.append(total)

            return min_list
    except:
        return "Did you break the break or should we continue?"

def magic_8_ball(my_question: str = "", fixed_list: list = None):
    '''
    -function to return a random answer from a list of answers
    :param list: - <list> of <value(s)> to give a fixed value out fo the <list> of
    answers
    :param value: - <value> that is the question that is asked
    :return:
    '''

    answers = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", 
               "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
                "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
                "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.",
                "Outlook not so good.", "Very doubtful."]

    try:
        if not isinstance(my_question, str):
            raise TypeError("I have spoken.")
        if my_question == "":
            raise ValueError("I have spoken.")
        if fixed_list == []:
            raise ValueError("I have spoken.")
        if fixed_list != None:
            # comment next if/return to observe error
            for val in fixed_list:
                if val == -1:
                    my_question.remove(val)
                if not isinstance(val, int):
                    raise TypeError("I have spoken.")
                if val < -1:
                    raise ValueError("I have spoken.")
                if val > 20:
                    raise ValueError("I have spoken.")
            random_num = random.randint(0, len(fixed_list))
            random_fixed_ans = fixed_list[random_num - 1]
            return answers[random_fixed_ans]
            
        if fixed_list == None:
            random_num = random.randint(0,19)
            return answers[random_num]
    except Exception as e:
        return e
    
def all_pairs( s1=[],s2="" ):
    '''
    - function which creates a list with all pairs of elements from sequences ‘s1’
    and 's2'
    '''

    try:
        if s1 == [] and s2 == "":
            return (False, [])
        list1 = []
        i = 0
        while i < len(s2):
            list1.append(str(s2[i]))
            i += 1

        list2 = []
        i = 0
        while i < len(s1):
            str1 = str(s1[i])
            for val in list1:
                list2.append(str1 + val)
            i += 1
        if len(list2) != 0:
            return (False, list2)
    except:
        return (True, [-1])
        

