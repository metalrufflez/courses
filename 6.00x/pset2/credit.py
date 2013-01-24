balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0

for month in range(12):
	thisMonthPayment = balance * monthlyPaymentRate
	totalPaid += thisMonthPayment

	balance -= thisMonthPayment
	monthInterest = balance * (annualInterestRate/12)
	balance += monthInterest

	print "Month: " + str(month+1)
	print "Minimum monthly payment: %.2f" % thisMonthPayment
	print "Remaining Balance: %.2f" % balance


print "Total Paid: %.2f" % totalPaid
print "Remaining Balance: %.2f" % balance
