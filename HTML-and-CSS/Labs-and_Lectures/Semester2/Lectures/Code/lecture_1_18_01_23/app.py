# A. Variables and assignment

x = 2
y = 3.7
print( x )
y = x + y + 1
print( y )

# B. Data types

# integers (ints) - whole numbers
# floating point numbers (floats) - numbers with a decimal part
#  operations: + - * / // % (modulus, remainder)

# Booleans - True, False NOT true, "True", "true"
#  operations: and or not

b1 = True
b2 = False
print( b1 and b2 )

# strings - sequences of characters, enclosed in quotes
#  operations, e,g + (concatenation)

s1 = 'abc'
s2 = 'defgh'
s3 = s1 + s2
print( s3)

# s4 = 2 + "3" error
z = 2 + int("3")
s4 = str(2) + "3"

s5 = """This is a very long string. IN fact, it is so strong that it goes all the way to the edge of the 
screen at which point I pressed Enter in order to continue on the next line. ACtually, there's even
a third line."""

# C. Collections of data
#  lists, dictionaries, sets, tuples

# Lists - sequences of data enclosed in []

days = [31, 28, 31, 30]
months = ["Jan", "Feb", "Mar"]
lists_of_lists = [ ["Ann", "Ben"], ["Col", "Deb", "Ed"], ["Flo"] ]

# operations: +

months = ["Jan", "Feb", "Mar"] + ["Apr", "May"]

#Visit each item

for d in days: 
    print(d)

# Indexing - by position, starting at zero
print("Feb has", days[1], "days")
days[1] = 29
print(days)

# DIctionaries, collection of key-value pairs, enclosed in ()
#  keys must be unique

months_dict = {"Jan":31, "Feb":28, "Mar":31, "Apr":30}

# Indexing - by position, starting at zero
print("Feb has", days [1], "days")
days [1] = 29
print(days)

# Dictionaries, collection of key-value pairs, enclosed in ()
# keys must be unique

months_dict = {"Jan" : 31, "Feb" : 28, "Mar" : 31, "Apr" : 30}

# Indexing, by key

print( months_dict ["Feb"] )
months_dict["Feb"] = 29

# Visit each key
 
for m in months_dict:
    print( m, months_dict[m])
# D. Functions
heights = [153, 189, 189, 165]
ages = [18, 19, 18, 20, 21, 18]

# Bad code

result = 0
for h in heights:

    result = result + h
print(result)

result = 0
for a in ages:

    result = result + a
print(result)

# Good code

def add_list(numbers):
    result = 0
    for n in numbers:
        result = result + n

    return result

print( add_list(heights) )
print( add_list(ages) )

# Modules - separate file of functions (and other stuff)

from lib import mean, median

print( mean(ages) )
print( median(ages) )

# Modules can be written by you
# Some modules come 'for free' with Python
# Some modules you install separately

from random import randint

roll = randint(1, 6)
print("you rolled a", roll)