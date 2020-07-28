from nltk.corpus import words
setofwords = set(words.words())
def dict_check(list):
    valid_words=[]
    for l in list:
        if l in setofwords:
        	valid_words.append(l)
    return valid_words