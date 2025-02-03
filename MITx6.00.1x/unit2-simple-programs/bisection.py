low = 1
high = 100
guess = int(high / 2)

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number {0}?".format(guess))
    print("Enter 'h' to indicate the guess is too high.", end=" ")
    print("Enter 'l' to indicate the guess is too low.", end=" ")
    print("Enter 'c' to indicate I guessed correctly.", end=" ")

    # make response
    response = None

    # get feedback 
    while response not in ["h", "l", "c"]:
        response = input("")
        if response not in ["h", "l", "c"]:
            print("Sorry, I did not understand your input.")
            break
    
    # figure out next guess
    if response == 'c':
        print("Game over. Your secret number was: {0}".format(guess))
        break
    elif response == 'h':
        high = guess
    elif response == 'l':
        low = guess


    # now make the new guess
    guess = int((high + low) / 2)
