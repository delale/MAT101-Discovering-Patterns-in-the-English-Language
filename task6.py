"""
Task 6
Refine the function defined in Task 1: Define a function that, given the same input as in Task 2,
outputs a list of all the sentences containing the word in question.
Make sure that your function removes unnecessary line breaks.
"""


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
    """
    file = open(path, 'r', encoding='utf-8')  # the encoding needs to be adjusted, debending on how the novel is saved
    content = file.read()
    sentences_with_keyword = []
    result = []

    # make keyword lower, so that capitalization doesn't become an issue
    keyword = keyword.lower()
    # insert markers for alternative punctuation, so that origianal punctuation can be restored in the end
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

# testing
print(instances('Wuthering Heights.txt', 'lobby'))
# Error: there are actually two instances of the word 'lobby'.
# the problem is the second one is 'lobby,' so with line 30 we are excluding it. 
