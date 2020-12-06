"""
The goal of this task is to define a function that finds all instances of a given word
in a given text file. More concretely, define a function that takes a word and the file
path to a text file as input. Its output should be a list of pairs, each consisting of a
line in which the word occurs and the corresponding line number.

For the doctest to work, please make sure the file 'Wuthering Heights.txt' is in the directory.
"""

def instances(word, path):
    """
    Takes a word as input and finds all lines that contain the word
    returning a list of lists where each list is composed of 2 elements:
    the line and the line number

    >>> instances('admired', 'Wuthering Heights.txt')
    [('the heating spices; and admired the shining kitchen utensils, the', 1839), ('expedition to the Crags.  While I admired and they laboured, dusk drew', 11534)]
    >>> instances('vast', 'Wuthering Heights.txt')
    [('row, on a vast oak dresser, to the very roof.  The latter had never been', 120)]
    >>> instances('working', 'Wuthering Heights.txt')
    [('working at a fence round a plantation, on the borders of the grounds.  I', 6837), ('occupations of working on the farm and lounging among the moors after', 7008), ('train myself to be capable of working like Hercules, and when everything', 11564)]

    One case in which it does not work as perhaps expected is with words that contain apostrophes, e.g. "isn't".
    To avoid complications with cases where apostrophes are used as quote marks, the program just simply treats 
    such words as if the apostrophe were removed, e.g. "isn't" becomes "isnt".
    Hence the following test fails:
    >>> instances("mustn't", "Wuthering Heights.txt")
    [("You mustn't think I care little for Catherine, because I behaved so", 6099), ('\'"I\'ll not hold my tongue!" I said; "you mustn\'t touch him.  Let the door', 6268), ("speak so to me?  Mustn't he be made to do as I ask him?  You wicked", 6965), ("I whispered Catherine that she mustn't, on any account, accede to the", 7643), ("my arm over her shoulder.  'You mustn't cry because papa has a cold; be", 8245), ("and to put her back in the stable: you mustn't scold him either, mind.  I", 8841), ("'I knew now that I mustn't tease him, as he was ill; and I spoke softly", 8964), ('me, and that he mustn\'t invent any more falsehoods on the subject."', 9074), ("come to the Grange?  Oh, darling Catherine! you mustn't go and leave,", 9760)]
    Instead, to get the desired result, one must search for "mustnt".

    :param word str: word to search
    :param path str: path of the file in which to search the word
    :return list: a list of lists where each element is a list of
                  line and line number where the word was found
    """

    # raise error when word or path are not strings
    if type(path)!=str or type(word)!=str:
        raise ValueError('"path" and "word" must be of type string')

    f = open(file=path, encoding="utf8")
    lines = f.readlines() # list of all lines in file
    f.close()
    out = []

    # itertiong through the lines: i=line number, l=line
    for i,l in enumerate(lines):

        # create list containing all the words in the line, all in lower case, with non-alphabetic characters removed
        line = "".join([character.lower() for character in l if character.isalpha() or character == " "]).split()

        if word.lower() in line:
            # if the word is found in the line -> append a list [line, line number]
            out.append((l.replace('\n', ''), i))

    # different returns if the word was ever found in the file or not
    if len(out) > 0:
        return out
    else:
        return "{} is not found in the file {}".format(word, path)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
