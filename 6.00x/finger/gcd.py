def gcdRecur(a, b):

	if b == 0:
		return a

	return gcdRecur(b, a % b)

print gcdRecur(9269826459862**22,298737692645**89)
