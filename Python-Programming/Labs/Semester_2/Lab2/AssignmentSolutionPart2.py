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
                avBouts.append(av)

    meanPerPatient = []
    for patientId, av in enumerate(avBouts):
        meanPerPatient.append([patientId, av])

    inFile.close()

    return meanPerPatient


print(meanBoutsPerPatient())

def writeToFile(meanPerPatient):

    inFile = open("meanBoutsPerPatient.txt", "w")

    for entry in meanPerPatient:
        patientId, mean = entry
        inFile.write("Patient %s had %s inflammatory bouts on average. \n" % (patientId + 1, mean))

meanPerPatientData = meanBoutsPerPatient()
writeToFile(meanPerPatientData)