# Q1

# first read in the data from the dna file
inFile = open("dna.txt", "r")

# next, read() is used to read the entire contents of the dna file into a single string
dnaString = inFile.read()
# the string is now separated into a list of values
# each value in the list is a different person's dna sequence
# they were separated into paragraphs - '\n\n' code equivalent of what the user would see as a new line
# '\n' would take the following text onto a new line, and another right after would take the text onto another new line
# the effect of this would appear as a new paragraph as there is an empty line in-between the people's dna sequence
dna = dnaString.split("\n\n")
# the dna sequence of each person is found in another of lines, not just one
# so here we are removing these new lines '\n' so each value in the list is all in one single line when displayed
dnaformatted = []
for individualDNA in dna:
    individualDNA = individualDNA.replace("\n", "")
    dnaformatted.append(individualDNA)

# now enumerated will be used to read each persons dna sequence, with each person being numbered
for personID, dna in enumerate(dnaformatted):
    print (personID, ":", dna)
inFile.close()

# Q2

def meanBoutsPerPatient():

    inFile = open("InflammatoryIBS.csv", "r")
    ibsString = inFile.read()

    ibsBouts = ibsString.split("\n")

    ibsBoutsInInts = []
    for patient in ibsBouts:
        patientBoutList = patient.split(",")
        patientIntsList = []
        for bout in patientBoutList:
            intBout = int(bout)
            patientIntsList.append(intBout)
        ibsBoutsInInts.append(patientIntsList)

    totalBouts = []
    for patient in ibsBoutsInInts:
        totalBouts.append(sum(patient))

    avBouts = []

    for total in totalBouts:
        for patient in ibsBoutsInInts:
            if totalBouts.index(total) == ibsBoutsInInts.index(patient):
                av = total / len(patient)
                avBouts.append(round(av))

    for patientId, av in enumerate(avBouts):
        print( "Patient", patientId + 1, "had", av, "inflammatory bouts on average.")

    inFile.close()

def meanBoutsAcrossAllPatients():

    inFile = open("InflammatoryIBS.csv", "r")
    ibsString = inFile.read()

    ibs = ibsString.replace("\n", ",")

    ibsList = ibs.split(",")

    totalIbs = 0

    for bout in ibsList:
        totalIbs += int(bout)

    lenIbsList = len(ibsList)

    avIbs = round(totalIbs / lenIbsList)

    inFile.close()

    print("The average of the inflammatory bouts on this trial medication is:", str(avIbs))

meanBoutsPerPatient()
meanBoutsAcrossAllPatients()



