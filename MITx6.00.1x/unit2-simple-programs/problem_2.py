balance = 3329
annualInterestRate = 0.2
result = 310


# balance = 4773
# annualInterestRate = 0.2
# result = 440




# monthly interest rate
mir =  annualInterestRate / 12

paid_off = False
maybe_payment = 10
_balance = balance


# now just simulate months
while not paid_off:

    # simulate a year
    for month in range(1, 13):

        # unpaid balance - (Previous balance) - (Minimum monthly payment)
        unpaid_balance = _balance - maybe_payment

        # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
        _balance = unpaid_balance + (mir * unpaid_balance)
    
    # if balance greater than 0 we are not paid off.
    if _balance > 1:
        maybe_payment += 10

        # reset the balance 
        _balance = balance
    else:
        # congratulations - welcome to your debt free world
        paid_off = True

print("Lowest Payment:", maybe_payment)