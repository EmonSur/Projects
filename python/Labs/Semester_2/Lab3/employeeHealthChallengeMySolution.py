import copy

stepData = [[9000, 10000, 10000, 11100, 3400], [2000, 2000, 3400, 5400, 12300], [11000, 12000, 13435, 11234, 10347], [9800, 9500, 8900, 10002, 10054], [4500, 5697, 7898, 8796, 10324], [7600, 12000, 12345, 11234, 9820], [13560, 14000, 13000, 11000, 10986], [7600, 4356, 9820, 10980, 11240], [10005, 11112, 12243, 13354, 9002], [10340, 10546, 10890, 10002, 9002]]
# my first attempt at this included the following - stepData = stepData2
# i realized that this method does not make a copy of the list, but instead makes a new reference to the list
### [this is also the case for other immutable objects - meaning the contents of which can be changed after is has been created. Dictionaries would be the other type]
### [strings, integers and tuples are mutable, meaning the contents of which cannot be changed after it has been created, they do allow modifications, e,g, add, remove, performing operations on it.]
### [it just cannot be said the contents of the mutable object are something else after it has been created, e.g. a = "hello". we cannot say a is now = "hi". there is ways to get around this however]
# so if to keep the contents of the original list in stepData2, this will not do, as any changes made to stepData, will also make changes to stepData2
# making a deep copy of the list, as seen below is the only reliable of ensuring nothing in stepData2 is changed, besides using loop to make a new list
# stepData2 = copy.deepcopy(stepData)
# this method is only needed when changing the contents of the original list. the following code has been modified so the original list is no longer being modified. so copy.deepcopy() is not needed anymore

#(a) The number of week-days on which at least 100,000 steps were made cumulatively by all employees i.e. Add Columns.
numWeekdays = 0

for day in range (len(stepData[0])):
	weekdayTotal = 0
	for employee in range(len(stepData)):
		weekdayTotal += stepData [employee][day]
		
	if weekdayTotal > 100000:
		numWeekdays += 1
		
print ("Number of weekdays over 100000: ", numWeekdays) 

#(b) The number of the employee who took the most steps in the week (assume there can only be one). i.e. add the row and check for max

employeeMostStepsID = 0
employeeMostSteps = 0

totalStepsPerEmployee = []

for employee in stepData:
    totalSteps = 0
    for day in employee:
        totalSteps += day
    totalStepsPerEmployee.append(totalSteps)

for step in totalStepsPerEmployee:
    if employeeMostSteps < step:
        employeeMostSteps = step
        employeeMostStepsID = totalStepsPerEmployee.index(step)

print("Employee ID with most steps is: ", employeeMostStepsID, "with", employeeMostSteps, "steps")