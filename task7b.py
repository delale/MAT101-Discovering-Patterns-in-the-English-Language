import matplotlib.pyplot as plt
import glob
from cleaning import cleanGut
'''
This program calculates the average sentence length authors use in a book.
Any Book as text file can be entered with the Title: Author_NAMEOFAUTHOR_BOOKTITLE (NAMEOFAUTHOR and BOOKTITLE can be chosen)

'''

def words_per_sentence(path):

    # raise error when word or path are not strings
    if type(path) != str:
        raise ValueError('"path" must be of type string')

    f = open(file = path, encoding = "utf8")
    book = cleanGut(f)
    f.close()

    sentencecount = book.count(".")  + book.count("?") + book.count("!")      #Counts sentences
    for ch in book:
        if ch.isalpha() == False:
            book = book.replace(ch, "") # treats don't as dont

    wordlist = book.lower().split()                   # Calculates amount of total words
    rubbish = 0                                       #              
    for i in wordlist:                                 #
        if i != 'i' and i != 'i' and len(i) <= 1:     #
            rubbish += 1                              #
    totalwords = len(book.split()) - rubbish          #

    return totalwords/sentencecount                   #Returns average words per sentence

filelist = glob.glob(" *.txt")        #Takes all filenames

for i in range(len(filelist)):              
    if filelist[i][0:6] == "Author":            #Identifies files we wanna analyse the authors sentence length
        authorlist = filelist[i].split("_")     #Splits the file name at "_"'s
        w_p_s = round(words_per_sentence(filelist[i]), 3)     #Words per sentence function get called
        print("The author {} uses an average of {} words a sentence, in his book '{}'."  .format(authorlist[1] , w_p_s , authorlist[2][:-4]))

