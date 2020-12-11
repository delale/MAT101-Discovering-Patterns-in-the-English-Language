def cleanGut(fyle):
    """
    Function to clean in a general sense Project Gutenberg texts.
    Reads in the parsed file.
    Finds START and END by looking for ***.
    Removes some of the unnecessary words (not all).
    DOES NOT REMOVE PUNCTUATION.

    :param fyle str: Gutenberg text file to be cleaned
    :return str: cleaned Gutenberg text file with each line separated by '\n'
    """

    content = fyle.read()

    unnecessary = ("CHAPTER", "SECTION", "BOOK", "PARAGRAPH", "CONTENTS", "POEM") # set of unecessary words
    START = content.rfind("***", 0, len(content) // 2) # finds the start
    END = content.find("***", len(content) // 2) # finds the ending
    if START==-1 or END==-1: # if the file is not from Gutenberg Project
        return content

    # slicing
    lyst = content[START + 3:END].split('\n') # splitting into lines

    toberm = [] # list of lines to be removed (containing unnecessary)
    for i, line in enumerate(lyst):

        if line.isupper():
            for un in unnecessary:
                if un in line:
                    toberm.append(i)

    toberm = set(toberm)
    clean = [x for i,x in enumerate(lyst) if i not in toberm]

    return "\n".join(clean)

if __name__=="__main__":

    cleanGut(open("Wuthering Heights.txt", 'r'))