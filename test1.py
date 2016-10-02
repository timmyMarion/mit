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
print(applyF_filterG(L, f, g))
print(L)
