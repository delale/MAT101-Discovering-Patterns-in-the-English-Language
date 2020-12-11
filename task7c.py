import nltk
from nltk.tokenize import word_tokenize
from cleaning import cleanGut

def wordtypes(path):
    """
    Using the module nltk to analyze a text file and assign word type tags to each word in the text file
    depending on the context.

    Problems:
    This module isn't available everywhere. So for best result, run in Jupyter Notebook.
    Additionally, the accuracy of the module varies, because of the difficulty of understanding
    the context of the word used.
    e.g. the word 'help' can be a noun or a verb depending on the context.

    Variables:
    content = the content of the text file
    l = a temporary list with all alphabetic characters of the content
    pure_content = the content of l as a string
    tags = a list of tags that the module nltk will assign to the words in the text
    tag_names = a list of the true meanings of the tags
    h = a list of all words and their tags
    result = dictionary of all words sorted according to word type

    :param path: open any text file
    :return: dictionary of all words sorted according to word type
    """
    f = open(path, 'r', encoding="utf8")
    content = cleanGut(f)
    f.close()
    result = {}
    content = content.lower()
    #remove apostrophes so that the whole word is analyzed
    content = content.replace("'", '')
    #remove all other non-alphabetical characters
    for i in content:
        if i.isalpha() == False:
            content = content.replace(i, ' ')
            
    #these are the tags that the module nltk  automatically assigns to the words in the text file     
    tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP',
        'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$',
        'WRB']
    #tag_names is just a list of names for the tags above, that is more readable, bc the original tags don't make any sense
    tag_names = ['coordinating conjunction', 'cardinal digit', 'determiner', 'existential there', 'foreign word', 'preposition',
             'positive adjective', 'comparative adjective', 'superlative adjective', 'modal verb', 'singular noun',
             'plural noun', 'singular proper noun', 'plural proper noun', 'predeterminer', 'possessive ending',
             'personal pronoun(e.g. I, he, she)', 'personal pronoun(e.g. my, his, her)', 'positive adverb',
             'comparative adverb', 'superlative adverb', 'particle', 'to (e.g. to go to the store)', 'interjection',
             'regular verb', 'verb past tense', 'present participle verb', 'past participle verb',
             'singular verb present', 'third person singluar verb present', 'wh-determiner', 'wh-pronoun',
             'possessive wh-pronoun', 'wh-adverb']
    
    #here the tags are assigned to the words in the text file
    text = word_tokenize(content)
   
    h = nltk.pos_tag(text) #the output is a tuple (word, tag)// e.g. (car, NN)
    #here a dictionary is created with elements from tag names
    #keys = elements from tag_names
    #values = words from text file that were assigned to one of the tags
    for i in h:
        if i[1] not in tags:
            pass
        else:
            pos = tags.index(i[1])
            result[tag_names[pos]] = result.get(tag_names[pos], []) + [i[0]]
    
    return result
    
    
#example output:
#{'singular proper noun': ['Mr', 'Lockwood', 'Thrushcross', 'Grange'], 'personal pronoun(e.g. my, his, her)': ['your', 'my', 'my'], 'positive adjective': ['new', 'tenant', 'possible'], 'singular noun': ['sir', 'honour', 'arrival', 'hope', 'perseverance', 'occupation', 'yesterday'], 'personal pronoun(e.g. I, he, she)': ['I', 'myself', 'I', 'you', 'I', 'you'], 'singular verb present': ['do', 'have'], 'determiner': ['the', 'the', 'the', 'some'], 'preposition': ['of', 'as', 'after', 'that', 'by', 'in', 'of'], 'present participle verb': ['calling', 'soliciting'], 'positive adverb': ['as', 'soon', 'not'], 'to (e.g. to go to the store)': ['to'], 'regular verb': ['express'], 'past participle verb': ['inconvenienced', 'had'], 'verb past tense': ['heard', 'had'], 'plural noun': ['thoughts']}

# w = wordtypes(path)
def count_wordtypes(w):
    """
    Count the amount of words assigned to a certain word type and return as a dictionary
    Variables:
    e = new dictionary
    d = copy of output from wordtypes()
    :param w: output from wordtypes()
    :return: a list of tuples of the word tags and the amount of words in the text file that assigned to that specific word tag
    """
    #this is essentially a counter for the values of each key in the output of wordtagging()
    #the number of words that were assigned to a certain word type becomes the new value
    
    e = {}
    d = w.copy()
    d = d.items()
    for i in d:
        length = len(i[1])
        e[i[0]] = length
    
    result = sorted(e.items(), key=lambda x: x[1])
    return result

#example output:
#[('to (e.g. to go to the store)', 1), ('regular verb', 1), ('plural noun', 1), ('singular verb present', 2), ('present participle verb', 2), ('past participle verb', 2), ('verb past tense', 2), ('personal pronoun(e.g. my, his, her)', 3), ('positive adjective', 3), ('positive adverb', 3), ('singular proper noun', 4), ('determiner', 4), ('personal pronoun(e.g. I, he, she)', 6), ('singular noun', 7), ('preposition', 7)]

if __name__=="__main__":
    path = "Wuthering Heights.txt"
    wt = wordtypes(path)
    print(wt)
    print(count_wordtypes(wt))
