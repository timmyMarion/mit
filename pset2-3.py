balance = 999999
annualInterestRate = 0.18
months = 12
high = balance + (balance * annualInterestRate)
low = balance / 12
payment = (low + high) / 12
workingBalance = balance

while True:
    workingBalance = balance
    for x in range(months):
        workingBalance -= payment
        workingBalance += workingBalance * (annualInterestRate / 12)
    if round(workingBalance, 2) == 0:
        print("Lowest Payment : " + str(round(payment, 2)))
        break
    elif workingBalance < 0:
        high = payment
        payment = (low + high) / 2
    elif workingBalance > 0:
        low = payment
        payment = (low + high) / 2
