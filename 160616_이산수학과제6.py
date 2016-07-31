def foobar(L):
    for x in L:
        if (x[0] != x[1]) and ((x[1], x[0]) in L):
            return False
    return True
