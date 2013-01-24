def oddTuples(aTup):

	index = 0
	retuple = ()

	while index < len(aTup):
		if index % 2 == 0:
			print index

			retuple += (aTup[index],)

		index += 1

	return retuple

print oddTuples(('I'))
print oddTuples(('I','am','a','test','tuple'))
print oddTuples(('Master','Blaster'))
