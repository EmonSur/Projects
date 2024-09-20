def readFile (filename):
    inFile = open("books.txt","r", encoding = "utf-8")
    book = inFile.read()

    for character in '!?”“.,-\n\n':
        book = book.replace(character, '')

    words = book.split(" ")


    freq = {}

    wordcount = 0
    
    for value in words:
        if words.count(value) != 0:
            wordcount += 1
            word = value.lower()
            
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1

    v = list(freq.values())
 

    k = list(freq.keys())
    
    mostCommmon = (k[v.index(max(v))])

    inFile.close()
    return mostCommmon
    #return freq

wordCount = readFile ("books.txt")
print (wordCount)


# def readFile (filename):
#     #read the file and return a list of words.
#     inFile = open("books.txt","r", encoding = "utf-8")
#     words = inFile.read()

#     words = words.strip("\n")
#     words = words.split(" ")


#     inFile.close()
#     return words

# wordList = readFile ("books.txt")
# print (wordList)

# def depunctuate (words):
#     punctuation = [",", ".", "!", "?", "-", "'"]
#     #depunctuate the words and return a cleaned list