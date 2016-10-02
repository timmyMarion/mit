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

print(dict_interdiff({1: 1, 2: 2, 3: 3, 4: 4}, {1: 1, 2: 2, 3: 3, 4: 5, 6: 2}))

