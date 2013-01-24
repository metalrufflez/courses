def lenIter(aStr):

	count = 0

	while aStr != '':
		count += 1
		aStr = aStr[1:]

	return count

def lenRecur(aStr):

	if aStr == '':
		return 0
	else:
		return 1 + lenRecur(aStr[1:])

print lenRecur('')
print lenRecur('x')
print lenRecur('arara')
print lenRecur('o rato roeu a roupa do rei de roma')

