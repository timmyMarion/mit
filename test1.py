d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}


print(d1.keys())
print(d2.keys())

print(d1.items())
print(d2.items())

print(d1.values())
print(d2.values())


for k1, v1 in d1.items():
    print(k1, v1)

for k2, v2 in d2.items():
    print(k2, v2)
    if k2 not in d1.keys():
        print("not in d1: " + str(k2))

both = {}
one = {}
for k1, v1 in d1.items():
    if k1 in d2.keys():
        print("In d2 " + str(k1))
        both[k1] = v1
    else:
        one[k1] = v1
for k2, v2 in d2.items():
    if k2 in d1.keys():
        print("In d1 " + str(k2))
        both[k2] = v2
    else:
        one[k2] = v2
print(one)
print(both)

def dict_interdiff(d1, d2):
    """This function will take in two dictionaries and return 2 dictionaries.
    one  will have the keys that are unique to each dictionary
    both will have the keys that are in both dictionaries. """
    one = {}
    both = {}
    for k1, v1 in d1.items():
        if k1 in d2.keys():
            both[k1] = v1
        else:
            one[k1] = v1
    for k2, v2 in d2.keys():
        if k2 in d1.keys():
            both[k2] = v2
        else:
            one[k2] = k2
    return one, both

(dict_interdiff(d1, d2))
