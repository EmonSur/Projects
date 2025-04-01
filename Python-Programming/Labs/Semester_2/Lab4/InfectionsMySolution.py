def load_data (filename):

    #create a dictionary - let's call it Infections
    infections = {}

    #read in the data from the file - How should I read this?
    inFile = open(filename, "r")
    data = inFile.readlines()

    #get every line of data
    for d in data:
        d = d.strip("\n")
        #split it on the comma
        d = d.split(",")
        #get the key for the dictionary i.e. the county. remember to get rid of the spaces!
        areaName = d[0].strip()
        #now get the value to go with that key i.e. the cumulative infection rates. remember to get rid of spaces and \n
        cumulativeInfections = d[1:]
        #for every cumulative infection get rid of the spaces and \n and convert to an int
        # this is a way to do a certain action to every value in a list without using a previous favourite - appending to a new list
        for i in range(len(cumulativeInfections)):
            cumulativeInfections[i] = int(cumulativeInfections[i].strip("\n").strip())
        #now create the entry in the dictionary
        #dict[key] = value
        infections[areaName] = cumulativeInfections

    # return Infections
    return infections

def daily_cases (cumulative):
    print(cumulative)
    #create a new dictionary called newInfections
    newInfections = {}
    #for every case in the cumulative dictionary i.e. for every county
    # we can use .items() to the key and the value for each entrance into a dictionary
    for county, cumulativeCases in cumulative.items():
        newInfectionsPerCounty = []
        firstOccurrence = True
        latestOccurrence = cumulativeCases[0]
        #for every list of cumulative infection values
        for cumulativeValue in cumulativeCases:
            #if it's the first value recorded, take it as is. Record this in the newInfections dictionary as a new value
            if firstOccurrence:
                newInfectionsPerCounty.append(cumulativeValue)
                firstOccurrence = False
            #else get the current cumulative value
            else:
            #subtract the number from the day before
                newInfectionsPerCounty.append(cumulativeValue - latestOccurrence) 
            #append it to the county in newInfections
            latestOccurrence = cumulativeValue
        newInfections[county] = newInfectionsPerCounty

    #return the newInfections dictionary
    return newInfections

cumulativeInfections = load_data("occurences.txt")
newInfectionRates = daily_cases (cumulativeInfections)
print(newInfectionRates)

