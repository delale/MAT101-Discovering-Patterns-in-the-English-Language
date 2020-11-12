"""
Task 2
Compile a list of all the words that occur in a given text file.
More concretely, define a function that takes the file path to a text file as input and outputs a list of pairs,
each consisting of a word and the number of times the word occurs in the text. The list should be in decreasing order.
Even for longer texts, such as Wuthering Heights, the execution of your program should take less than 30 seconds.

"""
import operator ## for better dictionary sorting
from string import punctuation ## to remove punctuation

def occurences(path):
    """
    The function should analyze the whole text file and return a list of words that are in the text file
    and also the amount of times each word occurs.
    :param path: text file (in this case Wuthering Heights by Emily Bronte)
    :return: list of pairs (word, number of times the word occurs

    Variables:
    f = the text file
    content = content of the text file
    temp = new string in which all the non alphabetical characters were removed
    temp_list = list of the string 'temp'
    dict = dictionary of the pairs
    keys_to_be_deleted = characters that shouldn't be included in the list, because they aren't real words
    result = sorted dictionary according to the number of times the words occur
    """

    ## open the file, read it, make all characters lower-case
    file = open(path, 'r')
    content = file.read()
    content = content.lower()

    ## removing special characters without using for loops
    ## str.maketrans creates a translation mapping for translate method
    content = content.translate(str.maketrans(punctuation, " "*len(punctuation)))

    #add words to the list 'temp'
    temp_list = content.split(' ')

    #start creating pairs of words and the number of times they occurred
    dict = {} ## key=word, value=count

    for i in temp_list: ## Here I took away the j for loop since it was redundant
        if i.isalpha() and i not in dict:
            count = temp_list.count(i)
            dict[i] = count

    #delete all non_words such as '' and s (resulting after a split of words like misanthropist's
    ## took away this part since '' should already not be in the dictionary as indexes of the dictionary are
    ## only created if the key.isalpha() == True and single letters I think it's wiser to keep them and in case exclude
    ## them later (example: a would be useful to keep)

    file.close()

    #sort the pairs
    ## I sort the pairs already in the return statement with the sorted function for all items and sorting
    ## for the value of each key
    ## sorted(dict.items()) returns a list of ordered tuples (pairs) based on the key
    ## operator.itemgetter(1) takes the second value in each tuple
    ## this is then assigned to the key param in sorted()
    return sorted(dict.items(), key=operator.itemgetter(1), reverse=True)


"""
import timeit
from numpy import mean
t=[]
for i in range(10): # this is testing 10 times the time to run the function on the big file and then prints the mean
    t.append(timeit.timeit("occurences('wh_ebronte.txt')", setup="from __main__ import occurences", number=1))
print(mean(t))
"""