def readDraws(winnerNumbers):

    inFile = open(winnerNumbers, "r")

    lotteryDrawsStr = inFile.readlines()
    for winning in lotteryDrawsStr:
        winning = winning.strip("\n")
    print(lotteryDrawsStr)

    lotteryDraws = []
    for winningNos in lotteryDrawsStr:
        winningNos.split()
        print(winningNos)
        winningsNosList = []
        for number in winningNos:
            winningsNosList.append(number)

        lotteryDraws.append(winningsNosList)
        


    return lotteryDraws



# def checkWinners (hello):

#     return

# userLotteryNos = print(list(input("Please enter your lottery numbers: ")))


# print(checkWinners("hello"))

print(readDraws("lotteryNumbers.txt"))
