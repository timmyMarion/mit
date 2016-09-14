balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
months = 12

while months > 0:

    balance -= (balance * monthlyPaymentRate)
    balance += balance * (annualInterestRate / 12)
    months -= 1

print("Remaining balance: " + str(round(balance, 2)))