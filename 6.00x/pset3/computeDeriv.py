def computeDeriv(poly):
	result = []
	i = 1

	if len(poly) == 1:
		result.append(0.0)

	while i < len(poly):
		result.append(poly[i] * float(i))
		i += 1

	return result

poly = [-13.39, 0.0, 17.5, 3.0, 1.0]  

print computeDeriv(poly)
