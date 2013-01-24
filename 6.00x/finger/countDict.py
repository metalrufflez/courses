def howMany(aDict):
	sum = 0

	for d in aDict.values():
		for e in d:
			print e
			sum += 1

	return sum

def biggest(aDict):
	biggestSize = 0

	if len(aDict) == 0:
		return None

	for d in aDict:

		if len(aDict[d]) >= biggestSize:
			biggestSize = len(aDict[d])
			biggestIndex = d

		print d
		print len(aDict[d])
		print biggestSize
		print biggestIndex
		print

	return biggestIndex

dictLong = {'a': [16, 0], 'c': [2, 19, 13, 3, 4, 3, 1, 16, 11, 19], 'b': [12, 11, 17], 'e': [9, 16, 16, 3, 13, 2, 2, 17, 13], 'd': [10, 1, 19, 10, 11, 13, 9, 1]}

print biggest(dictLong)

