# This script calculates and returns the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months

balance = 3329            # the outstanding balance on the credit card
annualInterestRate = 0.2  # annual interest rate as a decimal

q = False
for i in range(10,500,10):
    if q != True:
        temp = balance
        for j in range(12):
                temp = temp - i
                temp = temp + (annualInterestRate/12)*temp
                if temp <= 0:
                    q = True
                else:
                    q = False
    else:
        print("Lowest Payment: " + str(i-10))
        break