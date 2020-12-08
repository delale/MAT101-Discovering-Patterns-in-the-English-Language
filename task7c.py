import nltk
from nltk.tokenize import word_tokenize

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
    file = open(path, 'r', encoding="utf8")
    content = file.read()
    l = []
    tags = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP',
        'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$',
        'WRB']
    tag_names = ['coordinating conjunction', 'cardinal digit', 'determiner', 'EX', 'foreign word', 'preposition',
             'positive adjective', 'comparative adjective', 'superlative adjective', 'modal verb', 'singular noun',
             'plural noun', 'singular proper noun', 'plural proper noun', 'predeterminer', 'possessive ending',
             'personal pronoun(e.g. I, he, she)', 'personal pronoun(e.g. my, his, her)', 'positive adverb',
             'comparative adverb', 'superlative adverb', 'particle', 'to (e.g. to go to the store)', 'interjection',
             'regular verb', 'verb past tense', 'present participle verb', 'past participle verb',
             'singular verb present', 'third person singluar verb present', 'wh-determiner', 'wh-pronoun',
             'possessive wh-pronoun', 'wh-adverb']
    result = {}
    for i in content:
        if i.isalpha() == False:
            l.append(' ')
        else:
            l.append(i)
    pure_content = ''.join(l)
    text = word_tokenize(pure_content)
    h = nltk.pos_tag(text)
    for i in h:
        pos = tags.index(i[1])
        result[tag_names[pos]] = result.get(tag_names[pos], []) + [i[0]]
    
    file.close()
    return result
    
    
#example output:
#{'singular proper noun': ['Mr', 'Lockwood', 'Thrushcross', 'Grange'], 'personal pronoun(e.g. my, his, her)': ['your', 'my', 'my'], 'positive adjective': ['new', 'tenant', 'possible'], 'singular noun': ['sir', 'honour', 'arrival', 'hope', 'perseverance', 'occupation', 'yesterday'], 'personal pronoun(e.g. I, he, she)': ['I', 'myself', 'I', 'you', 'I', 'you'], 'singular verb present': ['do', 'have'], 'determiner': ['the', 'the', 'the', 'some'], 'preposition': ['of', 'as', 'after', 'that', 'by', 'in', 'of'], 'present participle verb': ['calling', 'soliciting'], 'positive adverb': ['as', 'soon', 'not'], 'to (e.g. to go to the store)': ['to'], 'regular verb': ['express'], 'past participle verb': ['inconvenienced', 'had'], 'verb past tense': ['heard', 'had'], 'plural noun': ['thoughts']}

w = wordtypes()
def count_wordtypes(w):
    """
    Variables:
    e = new dictionary
    d = copy of output from wordtypes()
    :param w: output from wordtypes()
    :return: a dictionary of the word tags and the amount of words in the text file that assigned to that specific word tag
    """

    e = {}
    d = w.copy()
    d = d.items()
    for i in d:
        length = len(i[1])
        e[i[0]] = length
    return e
