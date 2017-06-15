# Write a program to calculate the credit card balance after one year if a person only pays 
# the minimum monthly payment required by the credit card company each month.

balance = 4213              #  the outstanding balance on the credit card
annualInterestRate = 0.2    #  annual interest rate as a decimal
monthlyPaymentRate = 0.04   #  minimum monthly payment rate as a decimal

itr = 0
ans = 0

for itr in range(12):
    print("Month: " + str(itr+1))
    minpayment = balance*monthlyPaymentRate
    ans += minpayment
    print("Minimum monthly payment: %.2f" % minpayment)
    balance = balance - minpayment
    temp = balance
    balance = temp + (annualInterestRate/12)*temp
    print("Remaining balance: %.2f" % balance)
print("Total paid: %.2f" % ans)
print("Remaining balance: %.2f" % balance)