'''
Task 5
Compile a list of all the words that occur in a given text file. More concretely, define a function that takes the file path to a text file as input and outputs a list of
pairs, each consisting of a word and the length of the word. The list should be in
decreasing order
'''
from cleaning import cleanGut

def Wordlist(Path):
    """
    Takes as input a path to a text file and returns a list of pairs containing all words
    and their length in decreasing order.

    :param Path str: text file path
    :return list: list of pairs (word, wordLength)

    >>> Wordlist('Test1.txt')
    [('there', 5), ('this', 4), ('why', 3), ('are', 3)]

    One might expect a word like "doesn't" to be counted as having 7 letters. 
    Since we're treating apostrophes as if they didn't exist, instead we will have "doesnt" in our list, with length 6.
    Likewise we will have "dont" as length 4 instead of "don't" with length 5.
    Therefore the following test fails:
    >>> Wordlist('Test2.txt')
    [('happens', 7), ("doesn't", 7), ('happen', 6), ("don't", 5), ('this', 4), ('that', 4), ('know', 4), ('does', 4), ('case', 4), ('why', 3), ('the', 3), ('not', 3), ('nor', 3), ('but', 3), ('to', 2), ('it', 2), ('be', 2), ('i', 1)]
    """
    # raise error when path is not string
    if type(Path) != str:
        raise ValueError('"path" must be of type string')

    fyle = open(Path, 'r', encoding='utf-8')  # Reading in Path
    Book = cleanGut(fyle)
    fyle.close()

    for character in Book:  # Getting rid of all the nonsense
        if character.isalpha() == False:
            
            if character=="'":
                Book = Book.replace(character, "") # handles doesn't as doesnt
            else:
                Book = Book.replace(character, " ") # punctuation to " "

    WordList = Book.lower().split()  # Makes Wordlist
    WordList = sorted(set(WordList))  # Makes sure its only one of each word
    ReturnList = []  # Second Empty List

    for word in WordList:  # Creates the Return Pairs, with word and length
        if len(word) == 1 and word != "a" and word != "i":  # Gets rid of small nonsense, besides the words a and i
            continue
        else:
            Pair = (len(word), word)  # Forms Pairs (wordlength and word)
            ReturnList.append(Pair)  # Puts them in return List

    ReturnList.sort()  # Sorts List
    Returnlist = [(x, y) for y, x in
                  ReturnList]  # Flips the Pair (just a detail)

    return Returnlist[::-1]

# doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
