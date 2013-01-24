def isPrime(n):
    if type(n) != int:
        raise TypeError()

    if n <= 0:
        raise ValueError()

    if n == 2:
        return True
    elif n < 2:
        return False
    else:
        for div in range(2, int(n**0.5+1)):
            if n % div == 0:
                return False

        return True
