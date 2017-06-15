# This script calculates and returns the minimum fixed monthly payment using bisection search
# needed in order pay off a credit card balance within 12 months

balance = 320000
annualInterestRate = 0.2

lower = balance/12
upper = (balance*(1+annualInterestRate/12)**12)/12
ans = 0

q = False

while q != True:
    x = (upper+lower)/2.0
    temp = balance
    for i in range(12):
        temp = temp - x
        temp = temp + (annualInterestRate/12)*temp
    if  temp <= 0:
        if abs(temp) <= 0.01:
            q = True
        else:
            upper =x
    else:
        lower = x
print("Lowest Payment: %.2f" % x)