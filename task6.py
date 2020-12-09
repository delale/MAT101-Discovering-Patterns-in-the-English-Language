"""
Task 6
Refine the function defined in Task 1: Define a function that, given the same input as in Task 1,
outputs a list of all the sentences containing the word in question.
Make sure that your function removes unnecessary line breaks.
"""

from cleaning import cleanGut

def instances(path, keyword):
    """
    The function should analyze the whole text file and return a list of sentences that contain a certain keyword.

    :param path: text file (in this case Wuthering Heights by Emily Bronte)
    :param keyword: keyword that is to be searched in text
    :return: list (sentences)

    Variables:
    f = the text file
    content = content of the text file
    list_content = list of sentences
    sentences_with_keyword = list of sentences which contain the keyword
    result = final list of sentences which contain the keyword, but with original punctuation restored

    >>> instances('Wuthering Heights.txt', 'lobby')
    ["  One stop brought us into the family sitting-room, without any introductory lobby or passage: they call it here 'the house' pre-eminently.", '  He had only then come from the library; and, in passing through the lobby, had noticed our talking and been attracted by curiosity, or fear, to examine what it signified, at that late hour.']
    >>> instances("Wuthering Heights.txt", "memories") 
    ['  That is the sole consideration which can make me endure the whelp: I despise him for himself, and hate him for the memories he revives!']
    """
    # raise error when word or path are not strings
    if type(path) != str or type(keyword) != str:
        raise ValueError('"path" and "keyword" must be of type string')

    file = open(path, 'r', encoding='utf-8')  # the encoding needs to be adjusted, depending on how the novel is saved
    content = cleanGut(file)
    file.close()

    sentences_with_keyword = []
    result = []

    # make keyword lower, so that capitalization doesn't become an issue
    keyword = keyword.lower()
    # insert markers for alternative punctuation, so that original punctuation can be restored in the end
    punctuation = ['ecsm.', 'gtsm.', 'slsm.', 'ccma']
    marks = ['!', '?', '--', ',']
    for k, v in enumerate(marks):
        content = content.replace(v, punctuation[k])
    content = content.replace('\n', ' ')
    # convert text into list, which is split into single sentences
    list_content = content.split('.')
    # first append all sentences containing keyword into the specified list
    for i in list_content:
        if keyword in i.lower():
            sentences_with_keyword.append(i)
    for i in sentences_with_keyword:
        i = i + '.'
        for k, v in enumerate(punctuation):
            if v in i:
                i = i.replace(v, marks[k])
        result.append(i)
    return result

# doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod()
