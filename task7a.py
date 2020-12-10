import matplotlib.pyplot as plt
import glob
from cleaning import cleanGut


'''
Task 7a

In this Task we wrote a program that tries to check if the use of a word changes over time.
The user can save any amount Books he wants in .txt format with the ending of a year number between 1820 and 1920.
Than he can enter a word and the program will show him how the percentage of the word (compared to total words in the book)
changes over time. It does of course depend a lot on the author and subject of the book, we just try to see in some examples if we can
figure out some basic trends of a worduse.

The files should be placed in the "Count" subdirectory and have names such as "Book[year].txt"

'''

def count(word, path):

    # raise error when word or path are not strings
    if type(path) != str or type(word) != str:
        raise ValueError('"path" and "word" must be of type string')

    f = open(file= path, encoding= "utf8")          
    book = cleanGut(f)
    f.close()

    for ch in book:
        if ch.isalpha() == False:
            
            if ch=="'":
                book = book.replace(ch, "") # handles doesn't as doesnt
            else: 
                book = book.replace(ch , " ") # punctuation -> " "

    wordlist = book.lower().split()
    rubbish = 0                                     #Removes single letters besides i and a
    for i in wordlist:                              #
        if i != 'i' and i != 'i' and len(i) <= 1:   #
            rubbish += 1                            #

    totalwords = len(book.split()) - rubbish        #Calculation of total words
    wordcount = book.lower().split().count(word)    #Gives how many times our word is in text
    return ((wordcount / totalwords)* 100)          #Returns percentage of the word compared to all words

word = "behold" # input("Which word do you wanna analyse? ")  #Depending if you want to let the user type in a word or not
filelist=glob.glob("./Count/*.txt")          #Makes a list of all text files

years = []                            #empty lists
wordpercentages = []                  #
for year in range(1820 , 1921):                     
    possible_path = "Book" + str(year) + ".txt"      
    for filepath in filelist:
        if possible_path in filepath:                            #If Book is found with right Title, it is added to our data set
            years.append(year)                                                  #Adds a year
            wordpercentages.append(round(count(word , filepath) , 5))      #Adds the Wordpercentage
plt.plot(years, wordpercentages)                                            #Plot
plt.xlabel("Years")
plt.ylabel("Percentage-use of word: " + word)
plt.title("Can we see the change of the use of a word over time?")
plt.show()
