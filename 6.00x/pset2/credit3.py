balance = 320000
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
lowerBound = balance/12
upperBound = (balance*(1+monthlyInterestRate)**12)/12
payment = (upperBound + lowerBound)/2.0

while True:
	tempBalance = balance

	for month in range(12):
		tempBalance -= payment
		monthInterest = tempBalance * (annualInterestRate/12)
		tempBalance += monthInterest

	if abs(tempBalance) < 0.01:
		break

	if tempBalance > 0:
		lowerBound = payment
	else:
		upperBound = payment

	payment = (upperBound + lowerBound)/2.0

print "Lowest Payment: " + str(round(payment,2))
