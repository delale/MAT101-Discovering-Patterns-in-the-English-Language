"""
The goal of this task is to define a function that finds all instances of a given word
in a given text file. More concretely, define a function that takes a word and the file
path to a text file as input. Its output should be a list of pairs, each consisting of a
line in which the word occurs and the corresponding line number.
"""

def instances(word, path):
    """
    Takes a word as input and finds all lines that contain the word
    returning a list of lists where each list is composed of 2 elements:
    the line and the line number

    :param word str: word to search
    :param path str: path of the file in which to search the word
    :return list: a list of lists where each element is a list of
                  line and line number where the word was found
    """

    # raise error when word or path are not strings
    if type(path)!=str or type(word)!=str:
        raise ValueError('"path" and "word" must be of type string')

    f = open(file=path)
    lines = f.readlines() # list of all lines in file
    f.close()
    out = []

    # itertiong through the lines: i=line number, l=line
    for i,l in enumerate(lines):

        if word.lower() in l.lower():
            # if the word is found in the line -> append a list [line, line number]
            out.append([l.replace('\n', ''), i])

    # different returns if the word was ever found in the file or not
    if len(out) > 0:
        return out
    else:
        return "{} is not found in the file {}".format(word, path)
