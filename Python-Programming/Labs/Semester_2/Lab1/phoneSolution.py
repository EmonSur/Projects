phone = {'.': 1, ',': 11, '?': 111, '!': 1111, ':': 11111, 'A': 2, 'B': 22, 'C': 222, 'D': 3, 'E': 33, 'F': 333, 'G': 4,
         'H': 44, 'I': 444, 'J': 5, 'K': 55, 'L': 555, 'M': 6, 'N': 66, 'O': 666, 'P': 7, 'Q': 77, 'R': 777, 'S': 7777, 'T': 8, 'U': 88, 'V': 888,
         'W': 9, 'X': 99, 'Y': 999, 'Z': 9999, ' ': 0}
        
#Ask the user for a message and save it in variable     hello world!
message = input("Enter in a message: ")
keyOutput = ""

#get every letter or character in that message
for character in message:

    #take into account that the key might be uppercase or lowercase
    character = character.upper()

    #use that character or letter as a key into dictionary to get the associated value
    #concatenate the key presses and display the value at the end 
    keyOutput += str(phone[character])

print(keyOutput)
