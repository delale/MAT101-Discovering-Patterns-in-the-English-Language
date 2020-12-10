"""
The goal of this task is to define a function that finds all instances of a given word
in a given text file. More concretely, define a function that takes a word and the file
path to a text file as input. Its output should be a list of pairs, each consisting of a
line in which the word occurs and the corresponding line number.

For the doctest to work, please make sure the files 'Wuthering Heights.txt' and 'Test3.txt' are in the directory.
"""

from string import punctuation

def instances(word, path):
    """
    Takes a word as input and finds all lines that contain the word
    returning a list of lists where each list is composed of 2 elements:
    the line and the line number
    >>> instances('admired', 'Wuthering Heights.txt')
    [('the heating spices; and admired the shining kitchen utensils, the', 1840), ('expedition to the Crags.  While I admired and they laboured, dusk drew', 11535)]
    >>> instances('vast', 'Wuthering Heights.txt')
    [('row, on a vast oak dresser, to the very roof.  The latter had never been', 121)]
    >>> instances('working', 'Wuthering Heights.txt')
    [('working at a fence round a plantation, on the borders of the grounds.  I', 6838), ('occupations of working on the farm and lounging among the moors after', 7009), ('train myself to be capable of working like Hercules, and when everything', 11565)]
    
    The following test fails because of the way that we handle apostrophes (i.e. treating them as if they weren't there).
    We get a some false positives, in this case line 2, which is included because of the word "I'll".
    >>> instances("ill", "Test3.txt")
    [('I feel ill.', 1), ("'You're ill'", 4)]


    :param word str: word to search
    :param path str: path of the file in which to search the word
    :return list: a list of lists where each element is a list of
                  line and line number where the word was found
    """

    w = word # copy to work on, word = original for return
    # raise error when word or path are not strings
    if type(path)!=str or type(word)!=str:
        raise ValueError('"path" and "word" must be of type string')

    f = open(file=path, encoding="utf8")
    lines = f.readlines() # list of all lines in file
    f.close()
    out = []

    # itertiong through the lines: i=line number, l=line
    for i,l in enumerate(lines):
        lori = l # copy of original
        l = l.translate(str.maketrans(punctuation.replace("'",""), " "*(len(punctuation)-1))) # punctuation except '-> " "
        w = w.translate(str.maketrans(punctuation.replace("'",""), " "*(len(punctuation)-1)))
        l = l.replace("'", "").lower() # ' -> None
        w = w.replace("'", "").lower()

        # create list containing all the words in the line, all in lower case, with non-alphabetic characters removed
        line = l.split()

        if w.lower() in line:
            # if the word is found in the line -> append a list [line, line number]
            out.append((lori.replace("\n", ''), i+1)) # i+1 so it returns the exact line num. in the file

    # different returns if the word was ever found in the file or not
    if len(out) > 0:
        return out
    else:
        return "{} is not found in the file {}".format(word, path)


if __name__=="__main__":
    import doctest
    doctest.testmod()
