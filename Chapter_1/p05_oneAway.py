def oneAway(s1, s2):
    # Check if a string can be converted to another string with a single edit
    if len(s1) == len(s2):
        return oneAway_replace(s1, s2)
    if len(s1) + 1 == len(s2):
        return oneAway_insert(s1, s2)
    if len(s1) - 1 == len(s2):
        return oneAway_insert(s2, s1)
    return False


def oneAway_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        print(tuple(zip(s1,s2)))
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def oneAway_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


print(oneAway("pale", "bale"))
