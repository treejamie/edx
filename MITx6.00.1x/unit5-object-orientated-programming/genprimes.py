import math

def genPrime():
    """Starting from 0 return prime numbers in"""
    # start from 2
    generated = [2] 

    # now do the rest, slow style. Sieve of Eratosthenes would be the brave move
    for num in range(generated[:].pop(), 10000):
        if all(
                num % i !=0 for i in range(2, int(math.sqrt(num)) + 1 )
            ):
            generated.append(num)
            yield num



x = genPrime()

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())