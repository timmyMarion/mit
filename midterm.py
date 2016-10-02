def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    def lowbase(base, num):
        while True:
            for x in range(num):
                if pow(base, x) >= num:
                    return x

    step = lowbase(base, int(num))
    low = num - pow(base, step - 1)
    high = pow(base, step) - num

    if low < high:
        return step - 1
    elif low == high:
        return step - 1
    else:
        return step

# print(closest_power(20, 210.0))


listA = [1, 2, 3]
listB = [4, 5, 6]


def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''

    listC = []
    for x in range(len(listA)):
        listC.append(listA[x] * listB[x])
    answer = 0
    for x in range(len(listC)):
        answer += listC[x]
    return answer


# print(dotProduct(listA, listB))

L = [[2, -1, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 101, 10, 1, 1, 5, 4, 3]]


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    L.reverse()
    for x in range(len(L)):
        L[x] = L[x][::-1]
 #   print(L)


# deep_reverse(L)
# print(L)


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

def dict_interdiff(d1, d2):
    """This function will take in two dictionaries and return 2 dictionaries.
    one  will have the keys that are unique to each dictionary
    both will have the keys that are in both dictionaries. """
    one = {}
    both = {}
    for k1, v1 in d1.items():
        if k1 in d2.keys():
            both[k1] = f(d1[k1], d2[k1])
        else:
            one[k1] = v1
    for k2, v2 in d2.items():
        if k2 not in d1.keys():
            one[k2] = v2
    return both, one

def f(a, b):
    return a > b

# print(dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2}))

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    hold = L[:]
    for x in hold:
        if not g(f(x)):
            L.remove(x)
    if 0 == len(L):
        print("should be empty " + str(L))
        return -1
    else:
        print("Should just have answer " + str(L))
        return sorted(L)[-1]

def f(i):
    return i + 2

def g(i):
    return i > 5

L = [2, 1, 0, -1, -2, -3, -4, -5]
# print(applyF_filterG(L, f, g))
# print(L)

def flatten(aList):
    '''
    aList: a list
    Returns a copy of aList, which is a flattened version of aList
    '''

    if aList == []:
        return aList
    if isinstance(aList[0], list):
        return flatten(aList[0]) + flatten(aList[1:])
    return aList[:1] + flatten(aList[1:])