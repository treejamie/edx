import sys

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
result = 31.38

# balance = 484
# annualInterestRate = 0.2
# monthlyPaymentRate = 0.04
# result = 361.61


# base case is month twelve
for month in range(1, 13):
    # monthly interest rate
    mir =  annualInterestRate / 12

    # minimum monthly payment rate) x (Previous balance)
    min_payment = monthlyPaymentRate * balance

    # unpaid balance - (Previous balance) - (Minimum monthly payment)
    unpaid_balance = balance - min_payment

    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    balance = unpaid_balance + (mir * unpaid_balance)



print(round(balance, 2))

sys.exit()


# the argments for the function as the keys and expected results as values
tests = {
    (42, 0.2, 0.04): 31.38,
    (484, 0.2, 0.04): 361.61,
}

