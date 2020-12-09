"""
Task 2
Compile a list of all the words that occur in a given text file.
More concretely, define a function that takes the file path to a text file as input and outputs a list of pairs,
each consisting of a word and the number of times the word occurs in the text. The list should be in decreasing order.
Even for longer texts, such as Wuthering Heights, the execution of your program should take less than 30 seconds.

For the doctest to work, please make sure the file 'Test.txt' and 'Test2.txt' are in the directory.
"""

from operator import itemgetter ## for better dictionary sorting
from string import punctuation # for removing punctuation

def occurences(path):
    """
    The function should analyze the whole text file and return a list of words that are in the text file
    and also the amount of times each word occurs.
    :param path: text file
    :return: list of pairs (word, number of times the word occurs)

    >>> occurences('Test1.txt')
    [('there', 4), ('this', 3), ('why', 2), ('are', 1)]

    One case in which it does not work as perhaps expected is with words that contain apostrophes, e.g. "isn't".
    To avoid complications with cases where apostrophes are used as quote marks, the program just simply treats 
    such words as if the apostrophe were removed, e.g. "isn't" becomes "isnt".
    Hence the following test fails:
    >>> occurences('Test2.txt')
    [('happens', 3), ('to', 3), ('this', 3), ('case', 3), ('the', 3), ('be', 3), ('that', 2), ('happen', 2), ('it', 2), ('i', 1), ("doesn't", 1), ("don't", 1), ('but', 1), ('nor', 1), ('not', 1), ('does', 1), ('why', 1), ('know', 1)]
    
    """

    ## open the file, read it, make all characters lower-case
    file = open(path, 'r', encoding="utf8")
    content = file.read()
    content = content.lower()

    ## removing special characters without using for loops
    ## str.maketrans creates a translation mapping for translate method
    ## apostrophes are deliberately not in the list of punctuation and are instead removed afterwards
    ## this is so that e.g. "don't" becomes "dont" and not "don t"
    content = content.translate(str.maketrans("", "", punctuation)) # all punctuation is set to None

    #add words to the list 'temp'
    temp_list = content.split()

    #start creating pairs of words and the number of times they occurred
    dict = {} ## key=word, value=count

    ## use a set since this will contain only unique items
    ## = faster iteration in the for loop
    for i in set(temp_list):
        dict[i] = temp_list.count(i)


    file.close()


    ## Sorting the pairs already in the return statement with the sorted function for all items and sorting
    ## for the value of each key
    ## sorted(dict.items()) returns a list of ordered tuples (pairs) based on the key
    ## operator.itemgetter(1) takes the second value in each tuple
    ## this is then assigned to the key param in sorted()
    return sorted(dict.items(), key=itemgetter(1), reverse=True)

"""
# time testing
import timeit
from numpy import mean
t=[]
for i in range(10): # this is testing 10 times the time to run the function on the big file and then prints the mean
    t.append(timeit.timeit("occurences('Wuthering Heights.txt')", setup="from __main__ import occurences", number=1))
print(mean(t))
"""

# doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
