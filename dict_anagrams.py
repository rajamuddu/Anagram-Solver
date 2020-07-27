from dict_check import dict_check 
def dict_anagrams(word):
    """ Generate all of the anagrams of a word. """ 
    if len(word) < 2:
        return word
    else:
        temp=[]
        for i, letter in enumerate(word):
            if not letter in word[:i]: #avoid duplicating earlier words
                for j in dict_anagrams(word[:i]+word[i+1:]):
                    temp.append(j+letter)
        return temp


if __name__ == "__main__":
    list=dict_anagrams("tar")
    result=dict_check(list)
    print(result)
