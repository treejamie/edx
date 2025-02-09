"""
This is the same as the other one, buty this time
we are to increment in 0.01 increments and use a bisection
algo to find the target ammount.
"""

# Test Case 1:
# balance = 320000
# annualInterestRate = 0.2
# result = 29157.09

# Test Case 2:
balance = 999999
annualInterestRate = 0.18
result = 90325.03


# monthly interest rate
mir =  annualInterestRate / 12

paid_off = False
maybe_payment = 10 
_balance = balance
iterations = 0


# now just simulate months
while not paid_off:

    # reset the balance otherwise we will be here all day
    _balance = balance

    # simulate a year
    for month in range(1, 13):

        # unpaid balance - (Previous balance) - (Minimum monthly payment)
        unpaid_balance = _balance - maybe_payment

        # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
        _balance = unpaid_balance + (mir * unpaid_balance)

        # count the iterations
        iterations += 1
        

    # bisection stuff
    #print(" was: ", balance, end=' ')
    #print(" now: ", _balance, end=' ')
    #print(" paid: ", maybe_payment, end=' ')
    


    # If the balance is between -0.05 and 0.05 we are golden and have the answer
    if _balance > -0.05 and _balance < 0.05:
        paid_off = True
        #print(" <<<< PAID OFF >>>>")

    # if the balance is greater than zero we need to increase payments
    elif _balance > 0:
        #print("increase", end='')
        maybe_payment += (_balance / 2) / 12
    
    # if the balance is less than zero we need to decrease payments
    elif _balance < 0:
        #print("decrease", end='')
        maybe_payment -= (_balance / 2) / 12



    

print("Lowest Payment:", round(maybe_payment, 2))


#print("Iterations: ", iterations)
#print("expected: ", result)
#print("iterations: ", iterations)