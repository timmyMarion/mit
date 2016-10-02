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

#print(closest_power(20, 210.0))


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


#print(dotProduct(listA, listB))

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

