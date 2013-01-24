def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    rstr = ''
    while True:
        if len(s1) == 0:
            rstr += s2
            break
        elif len(s2) == 0:
            rstr += s1
            break
        else:
            rstr += s1[0] + s2[0]
            s1 = s1[1:]
            s2 = s2[1:]

    return rstr
            
def laceStringsRecur(s1, s2):
    #if len(s1) == 0:
        #return s2
    #elif len(s2) == 0:
        #return s1
    #else:
        #return s1[:1] + s2[:1] + laceStringsRecur(s1[1:],s2[1:])
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            return s2
        if s2 == '':
            return s1
        else:
            return s1[:1] + s2[:1] + helpLaceStrings(s1[1:],s2[1:],'')

    return helpLaceStrings(s1, s2, '')

print laceStringsRecur('t','caio')
