def selSort(L):
    count = 0
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i+1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
            count += 1

    print count

def newSort(L):
    count = 0
    for i in range(len(L) - 1):
        j=i+1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
                count += 1
            j += 1

    print count

def mySort(L):
    clear = False
    count = 0
    while not clear:
        clear = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                clear = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
                count += 1

    print count

array1 = [ 4, 3, 1, 0, 6, 2 ]
selSort(array1)
print array1

array2 = [ 4, 3, 1, 0, 6, 2 ]
newSort(array2)
print array2

array3 = [ 4, 3, 1, 0, 6, 2 ]
mySort(array3)
print array3
