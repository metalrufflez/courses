def isIn(char, aStr):

	if aStr == '' or (len(aStr) == 1 and aStr != char):
		return False
	else:
		middle = len(aStr)/2
		guess = aStr[middle]

		if guess == char:
			return True
		elif char < guess:
			return isIn(char,aStr[:middle])
		else:
			return isIn(char,aStr[middle:])

print isIn('f','')
print isIn('f','abcdefghijklmnopqrstuvwxyz')
print isIn('f','ajkmnp')
print isIn('f','bcdef')
