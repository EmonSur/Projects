L1 = [5, 8, 1, 9, 7, 3]
'''L1 = [5, 8, 1, 3, 7, 9] n=6
L1 = [5, 7, 1, 3, 8, 9]
L1 = [5, 3, 1, 7, 8, 9]'''

#Function definition
def SelectionSort (l):

	length = len(l)
	#for loop - number of rounds/iterations over the list we need to take
	for value in range(len(l)):
		#what's my largest number in the list? use max()
		largest = max(l[0:length])
		#What's the position of this number?
		posLargest = l.index(largest)
		#Where am I swapping it to?
		last = l[length - 1]
		#swap the number at the end of the list to the index where the largest number is
		l[posLargest] = last
		#swap the largest number to the 'end' of the list (remember the end is decreasing with each round/pass).
		l[length - 1] = largest
		length -= 1
		print(l)		#so that we can see the output after every round/pass/cycle/iteration
	
	return l

myList2 = SelectionSort (L1)
print(myList2)