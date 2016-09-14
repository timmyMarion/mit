balance = 3929
annualInterestRate = 0.2
months = 12
payment = 10
workingBalance = balance

while workingBalance >= 0:
    payment += 10
    for x in range(months):
        workingBalance -= payment
        workingBalance += workingBalance * (annualInterestRate / 12)
    if workingBalance <= 0:
        print("Lowest Payment: " + str(payment))
        break
    else:
        workingBalance = balance
