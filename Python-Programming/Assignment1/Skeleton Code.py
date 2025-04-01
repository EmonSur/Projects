#Name: Emon Monsur
#Student ID: 121367643
#Programme: 

########################## Question 1 ############################################
from asyncio import format_helpers


def calculate_score (board):

    symbols = {'#':5, 'O':3, 'X':1, '!':-1, '!!':-3, '!!!':-5}

    '''Calculate the score per row and append it to the rowTotals list'''

    #create an empty list to which the scores per row will be appended to
    rowTotals = []

    #use for loop to loop through row in board
    for row in board:
      #used to find the score per row
      scorePerRow = 0

      #use for loop to loop through the symbols in each row
      for symbol in row:
        #use the .get() method to get value associated with key (in this case the symbols on each row) in the dictionary
        scoreRow = symbols.get(symbol)
        #add the corresponding values of the keys to scorePerRow
        scorePerRow += scoreRow

      #if a scorePerRow value is less than 0, this value will be ammended to be equal to 0
      if scorePerRow < 0:

        scorePerRow = 0

      #add these scoresPerRow into a list which will contain all the scores per row
      rowTotals.append(scorePerRow)


    '''Calculate the score per column and append it to the colTotals list'''

    #create an empty list to which the scores per column will be appended to
    colTotals = []

    #use for loop to loop through column in board   
    for row in range (len(board[0])):
      #used to find the score per column
      scorePerCol = 0

      #use for loop to loop through the symbols in each column
      for value in range(len(board)):

        #create an empty string
        valueCol = ""
        #add the symbols to valueCOl
        valueCol += board [value][row]
        #use the .get() method to get value associated with key (in this case the symbols on each column) in the dictionary
        scoreCol = symbols.get(valueCol)
        #add the corresponding values of the keys to scorePerCol
        scorePerCol += scoreCol

      #if a scorePerCol value is less than 0, this value will be ammended to be equal to 0
      if scorePerCol < 0:

        scorePerCol = 0

      #add these scoresPerCol into a list which will all the scores per column   
      colTotals.append(scorePerCol)

    #return the row and column Totals
    return rowTotals, colTotals


rTotals, cTotals = calculate_score([["#", "!"],["!!", "X"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([["!!!", "O", "!"],["X", "#", "!!!"],["!!", "X", "O"]])
print (rTotals, cTotals)
rTotals, cTotals = calculate_score([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]])
print (rTotals, cTotals)

########################## Question 2 ############################################
def identifyPivot (L):

    #use try except to catch an exceptions
    try:

      #create a reversed list to simplify the process of examining if values after the pivot are equal to the ones before
      reversedL = list(reversed(L))

      #set counter
      i = 0
      #create a list that will contain all the steps of addition of list L
      allTheAdditions1 = []
      #each step of the addition
      subTotal1 = 0

      #use a while loop to create all the steps of addition
      while i < len(L):
        subTotal1 += L[i]
        #append these additions to the list of additions
        allTheAdditions1.append(subTotal1)
        #increment the counter
        i += 1


      #all these steps should be repeated with the reversed list
      i = 0
      allTheAdditions2 = []
      subTotal2 = 0

      while i < len(reversedL):
        subTotal2 += reversedL[i]
        allTheAdditions2.append(subTotal2)
        i += 1

      result = None
      # Go trough one array
      for i in allTheAdditions1:
        #check if an element is repeated in both lists - if there isnt any this means no pivot value exists in the list L
        #check if the pivot occurs in both lists at the same index
        if (i in allTheAdditions2) and (allTheAdditions1.index(i) == len(L) - allTheAdditions2.index(i) - 1):
          #Store the result and break the loop
          result = i

          break

      #get the index value for which the pivot occurs
      index1 = allTheAdditions1.index(result)
      #get the value that occurs in the original list at this index value
      pivot = L[index1]

      #return the pivot
      return pivot

    #if an exceptions occur - and if the input was a list of numbers, the only error than can occur is if there is no pivot point
    except:

      return - 1


print(identifyPivot([9,1,9])) #returns 1
# print(identifyPivot ([8,8,8,8])) #returns -1
print(identifyPivot ([1,2,4,9,10,-10,-9,3])) #returns 4
#this doesnt seem to work for whatever reason
print(identifyPivot ([7,-1,0,-1,1,1,2,3])) #returns 0