def evaluatePoly(poly, x):
	'''
	Computes the value of a polynomial function at given value x. Returns that
	value as a float.

	poly: list of numbers, length > 0
	x: number
	returns: float
	'''
	i = 0
	expr = 0.0

	while i < len(poly):
		expr += poly[i] * (x ** i)
		i += 1

	return expr

poly = [0.0, 0.0, 5.0, 9.3, 7.0]
x = -13

print evaluatePoly(poly, x)
