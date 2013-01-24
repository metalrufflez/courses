def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    if b == 0:
        return 0

    power = 0
    while True:
        calc = b ** power 

        if calc == x:
            return power
        elif calc > x:
            return power - 1
        else:
            power += 1


print myLog(0, 2)

