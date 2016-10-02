


def practice():
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati', 'two', 'three']}

    answer = None
    test = 0
    for x in aDict.keys():
        if len(aDict[x]) >= test:
            answer = x
            test = len(aDict[x])
    return answer

print(practice())