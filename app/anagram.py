def anagrams(word):
    """ Generate all of the anagrams of a word. """ 
    if len(word) < 2:
        return word
    else:
        temp=[]
        temp.append(word)
        for i, letter in enumerate(word):
            if not letter in word[:i]: #avoid duplicating earlier words
                for j in anagrams(word[:i]+word[i+1:]):
                    temp.append(j+letter)

    return list(set(temp)) 

