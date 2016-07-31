def isTransitive(L):
    for x in L:
        for y in L:
            if (x[1] == y[0]):
                if ([x[0], y[1]] not in L):
                        return False
    return True
