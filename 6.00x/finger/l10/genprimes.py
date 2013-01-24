def genprimes():
    yield 2

    num = 3
    while True:
        prime = True
        for div in range(2, int(num**0.5+1)):
            if num % div == 0:
                prime = False
                break
        if prime:
            yield num

        num += 1


for x in genprimes():
    print x
