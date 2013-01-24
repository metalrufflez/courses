def stdDev(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')

    lengths = []
    for l in L:
        lengths.append(len(l))

    return stdDev(lengths)

def devCoef(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return ((tot/len(X))**0.5) / mean

print devCoef([1,2,3])
print devCoef([11,12,13])
print devCoef([0.1,0.1,0.1])

