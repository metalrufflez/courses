balance = 320000
annualInterestRate = 0.2
calcBalance = 0
payment = 0.01

while True:
	tempBalance = balance

	for month in range(12):
		tempBalance -= payment
		monthInterest = tempBalance * (annualInterestRate/12)
		tempBalance += monthInterest

	if tempBalance > 0:
		payment += 0.01
	else:
		break

print "Lowest Payment: " + str(payment)
