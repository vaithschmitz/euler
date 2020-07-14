import numpy as np

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False



def largest_prime_factor(n):
    factors = []
    for num in range(2, n):
        if n % num == 0:
            # if n is prime add to list
            if is_prime(num) == None or is_prime(num) == True:
                factors.append(num)
            # check if list of primes multiplies up to n
            if np.prod(factors) == n: 
                factors.sort()
                print(factors[-1])
                return



largest_prime_factor(30)
