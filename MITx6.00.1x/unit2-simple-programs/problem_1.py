import sys
"""

  Test Case 2:
	      balance = 484
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      Result Your Code Should Generate Below:
	      Remaining balance: 361.61
"""


def debt(balance, apr, monthly_payment_rate, month=1):
    """Do this recursively you cold laiden muppet"""

    # base case is month twelve
    if month == 13:
         return round(balance, 2)

    # monthly interest rate
    mir =  apr / 12

    # minimum monthly payment rate) x (Previous balance)
    min_payment = monthly_payment_rate * balance

    # unpaid balance - (Previous balance) - (Minimum monthly payment)
    unpaid_balance = balance - min_payment

    # Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    updated_balance = unpaid_balance + (mir * unpaid_balance)

    #print("Month ", month, ": paid: ", min_payment, " | balance: ", balance)

    # recurse thyself
    # my eyes are also watering something rotten
    # - but, I and I should be honest here - not as bad as they were this morning

    return debt(updated_balance, apr, monthly_payment_rate, month + 1)


# the argments for the function as the keys and expected results as values
tests = {
    (42, 0.2, 0.04): 31.38,
    (484, 0.2, 0.04): 361.61,
}

# the function is debt.  Which is an oddly philosophical thing to say.
f = debt


for args, expected in tests.items():
        s = f(*args)
        # assert
        try:
            assert s == expected
            print("✅: success - {1} expected and {0} received".format(
                s,
                expected,
            ))
        except AssertionError:
            msg = "❌: error:\n\texpected: {1}\n\treceived: {0}. {2} ".format(
                s,
                expected,
                args
            )
            sys.exit(msg)