def probTest(limit):
    prob = 1.0/6
    rolls = 1
        
    while prob > limit :
        prob = prob * (5.0/6)
        rolls += 1

    return rolls
