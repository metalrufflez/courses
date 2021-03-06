# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    # FILL IN YOUR CODE HERE...
    i = 0
    expr = 0.0

    while i < len(poly):
        expr += poly[i] * (x ** i)
        i += 1

    return expr

# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    # FILL IN YOUR CODE HERE...
    result = []
    i = 1

    if len(poly) == 1:
        result.append(0.0)

    while i < len(poly):
        result.append(poly[i] * float(i))
        i += 1

    return result




# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
	'''
	Uses Newton's method to find and return a root of a polynomial function.
	Returns a list containing the root and the number of iterations required
	to get to the root.

	poly: list of numbers, length > 1.
		Represents a polynomial function containing at least one real root.
		The derivative of this polynomial function at x_0 is not 0.
	x_0: float
	epsilon: float > 0
	returns: list [float, int]
	'''
	iternum = 0

	while abs(evaluatePoly(poly,x_0)) > epsilon:
		x_0 = x_0 - evaluatePoly(poly,x_0)/evaluatePoly(computeDeriv(poly),x_0)
		iternum += 1

	return [x_0, iternum]

def computeRootCancer(poly, x_0, epsilon):
	ans = 0
	ansDeriv = 0
	power = 1
	numIterations = 0
	currentx = x_0
	while True:
		ansDeriv = 0
		ans = evaluatePoly(poly, currentx)
		derivList = computeDeriv(poly)
		ansDeriv += evaluatePoly(derivList,currentx)
		if abs(ans) >= epsilon:
			currentx = currentx - (ans/ansDeriv)
			power = 1
		else:
			break
		numIterations += 1
	return [currentx, numIterations]

poly = [-13.39, 0.0, 17.5, 3.0, 1.0] 
x_0 = 0.1
epsilon = .0001

print computeRoot(poly, x_0, epsilon) 
print computeRootCancer(poly, x_0, epsilon) 
