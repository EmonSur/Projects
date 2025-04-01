def load_data(filename):

	inFile = open ("occurences.txt", "r")
	# previously .read() was used to read the whole file as a single string
	# .readlines() instead read the whole file as a list of strings, where each string represents a new line in the file
	data = inFile.readlines()

	infectionDict = {}

	for d in data:
		# this removes the newline character from line d. this does not modify the d back in data, just for d in the for loop.
		d.strip("\n")
		# this will split the current line into a list of strings, using "," as a delimiter [one or more characters that are used to denote the bounds between regions in a text.]
		infection = d.split(",")
		# removes leading and trailing spaces from the first element of infections
		infection[0] = infection[0].strip()
		# extracts the cumulative infections from the infections list, starting from the second element
		cumulativeInfections = infection[1:]
		# now we will loop through the cumulativeInfections, removing 'whitespace' and newline characters, and turning the values into integers
		for i in range(len(cumulativeInfections)):
			cumulativeInfections[i] = int((cumulativeInfections[i].strip("\n")).strip())
		# finally a new entry is placed into the dictionary consisting of the new of the county as a key and the cumulativeInfections list as the value
		# we add to a dictionary by placing in [] after the dictionary the key name and equalling all this to the value in which the key relates to
		infectionDict[infection[0]] = cumulativeInfections

	inFile.close()
	return infectionDict
	
def daily_cases(cumulative):
	
	new = {}
	for case in cumulative:
		for pos in range (len(cumulative[case])):
			if pos == 0:
				new[case] = [cumulative[case][0]]
			else:
				caseOccurences = cumulative[case]
				diff = caseOccurences[pos] - caseOccurences[pos-1]
				new[case].append(diff)
	return new
	
cInfections = load_data ("occurences.txt")
print (cInfections)
newInfections = daily_cases (cInfections)
print (newInfections)
	
	
