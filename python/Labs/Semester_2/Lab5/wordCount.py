def readFile (filename):
    #read the file and return a list of words.
    inFile = open(filename, "r", encoding = "utf-8")
    book = inFile.read()

    bookInLowercase = ""
    for character in book:  
        if ord(character) >= 65 and ord(character) <= 90:
            bookInLowercase += chr(ord(character) + 32)
        else:
            bookInLowercase += character

    bookInLowercase.strip("\n\n")
    bookInLowercase = bookInLowercase.split()

    return bookInLowercase


def depunctuate (words):
    punctuation = [",", ".", "!", "?", "-", "'", "“", "”"]
    #depunctuate the words and return a cleaned list

    punctuationRemoved = []
    
    for word in words:
        wordPunctuationRemoved = "".join(char for char in word if char not in punctuation)
        punctuationRemoved.append(wordPunctuationRemoved)
    
    return punctuationRemoved

def countWords (words):
    #create a dictionary
    wordsCount = {}
    for word in words:
    #if a word doesn't exist add it as a key with 1 as a value
        if word not in wordsCount:
            wordsCount[word] = 1
    #it it does exist add 1 to the current count
        else:
            wordsCount[word] += 1


    mostCommonWord = None
    mostCommonCount = 0
    #process the dictionary to see which word has the highest count.
    for word, count in wordsCount.items():
        if count > mostCommonCount:
            mostCommonCount = count
            mostCommonWord = word
    #keep track of the highest word and associated count

    #write this to an output file
    if mostCommonWord is not None:
        outputFilename = "MostCommonWord.txt"

        with open(outputFilename, "w") as outputFile:
            outputFile.write(f"The most common word is '{mostCommonWord}' with a occurrence count of {mostCommonCount}")

#Main Program:

#read in the file to get a list of words (best use a function)
words_text = readFile("books.txt")

#depunctuate the lists of words
words_cleaned = depunctuate(words_text)

#count the words, calculate the max and write to a file
countWords(words_cleaned)
