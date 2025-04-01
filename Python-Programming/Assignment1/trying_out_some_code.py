l = [7,-1,0,-1,1,1,2,3]

l1 = list(reversed(l))

i = 0

total1 = []

subTotal1 = 0

while i < len(l):

    subTotal1 += l[i]

    total1.append(subTotal1)

    i += 1

i = 0

total2 = []

subTotal2 = 0

while i < len(l1):

    subTotal2 += l1[i]

    total2.append(subTotal2)

    i += 1

sameVAl = [i == j for i, j in zip(total1, total2)]

result = None
# Go trough one array
for i in total1:

    # The element repeats in the other list...
    if i in total2:
        
        if [i == j for i, j in zip(total1, total2)] == True:

        # and sameVAl == True: # and total1.index(i) == total2.index(i): #and total1.index(i) != len(total1) - 1:
        
        # if int(i) >= total1[-1] / 2:
            
        # if total1.index(i) == total2.index(i): # and total1.index(i) == [x for x in range(len(revTotal2)) if revTotal2[x] == i]: #i > total1[-1] / 2: # and total1.index[i] + (len(l) - total2.index[i]) + 2 == len(l) + 1:

        # Store the result and break the loop
    

            result = i

            print(result)

            break

index1 = total1.index(result)

pivot = l[index1]


print(pivot)