L1 = [5, 8, 1, 9, 7, 3]

def SelectionSort (l):

	#for loop - number of rounds/iterations over the list we need to take
	for noIterations in range (len(l)-1):
		#what's my largest number in the list?
		#slicing is used here to skip the the values at the end of the list that are already in order - the maximimums have already been put into their positions
		largest = max(l[0:len(l) - noIterations])

		#What's the position of this number?
		largestIndex = l.index(largest)
		
		#Where am I swapping it to?
		#swap the number at the end of the list to the index where the largest number is
		l[largestIndex] = l[len(l) - (noIterations + 1)]
		#swap the largest number to the 'end' of the list (remember the end is decreasing with each round/pass).
		l[len(l) - (noIterations + 1)] = largest
		
		print(l)
		
	return l

myList2 = SelectionSort (L1)
print ("\n\n", myList2)