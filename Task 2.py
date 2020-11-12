"""
Task 2
Compile a list of all the words that occur in a given text file.
More concretely, define a function that takes the file path to a text file as input and outputs a list of pairs,
each consisting of a word and the number of times the word occurs in the text. The list should be in decreasing order.
Even for longer texts, such as Wuthering Heights, the execution of your program should take less than 30 seconds.

"""
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
    file = open(path, 'r')
    content = file.read()
    #first make all the words lowercase
    content = content.lower()
    temp = []
    #remove all non-alphabetical characters and add words to the list 'temp'
    for i in content:
        for j in i:
            if j.isalpha() == False:
                new = i.replace(j, ' ')
                temp.append(new)
            else:
                new = i
                temp.append(new)
    temp = ''.join(temp)
    temp_list = temp.split(' ')
    #start creating pairs of words and the number of times they occurred
    dict = {}
    for i in range(0, len(temp_list)):
        for j in temp_list[i]:
            if j.isalpha() == False:
                new = temp_list[i].replace(j, '')
                temp_list[i] = new
    #count occurences
    for i in temp_list:
        if i not in dict:
            count = temp_list.count(i)
            dict[i] = count
        else:
            continue
    #delete all non_words such as '' and s (resulting after a split of words like misanthropist's
    keys_to_be_deleted = ['', 's']
    for i in keys_to_be_deleted:
        if i in dict:
            del dict[i]

    #sort the pairs
    sorted_values = sorted(dict.values())
    temp_result = {}
    for i in sorted_values:
        for k in dict.keys():
            if dict[k] == i:
                temp_result[k] = dict[k]
    result = []
    for i in temp_result.items():
        result.append(i)

    file.close()

    return result[::-1] #decreasing order
