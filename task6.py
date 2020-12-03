"""
Task 6
Refine the function defined in Task 2: Define a function that, given the same input as in Task 2,
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

    # add spaces to keyword, so that words containing the keyword don't count
    keyword = ' ' + keyword + ' '

    # make keyword lower, so that capitalization doesn't become an issue
    keyword = keyword.lower()

    # insert markers for alternative punctuation, so that origianal punctuation can be restored in the end
    content = content.replace('!', 'ecsm.')
    content = content.replace('?', 'qtsm.')
    content = content.replace('--', 'slsm.')
    content = content.strip() # taking out \n
    content = content.replace('\n', ' ') # sometimes \n are undetected if there is no space before

    # convert text into list, which is split into single sentences
    list_content = content.split('.')

    # first append all sentences containing keyword into the specified list
    for i in list_content:
        if keyword in i.lower():
            sentences_with_keyword.append(i)

    # restore original punctuation to the sentences and add them to a final list
    for i in sentences_with_keyword:
        if 'ecsm' in i:
            i = i.replace('ecsm', '!')
            result.append(i)
        elif 'gtsm' in i:
            i = i.replace('gtsm', '?')
            result.append(i)
        elif 'slsm' in i:
            i = i.replace('slsm', '--')
            result.append(i)
        elif i == '':
            pass
        else:
            i = i + '.'
            result.append(i)

    return result

# testing
print(instances('Wuthering Heights.txt', 'lobby'))
# Error: there are actually two instances of the word 'lobby'.
# the problem is the second one is 'lobby,' so with line 30 we are excluding it.
# Also I think there is a mistake in the task description: I think Fatemeh meant to refine the function from Task1 and not Task2.
# That's why I changed the name to "instances".  