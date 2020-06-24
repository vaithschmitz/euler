import numpy as np

# def is_prime(i):
#     for x in range(2, i):
#         # if 2 or 3
#         if i == 2 or i == 3: 
#             return True
#         # if divisible by 2 
#         elif i % 2 == 0 or i < 2: 
#             return False
#         elif x % 2 != 0:
#             # if not divisible by 2 and i divisible by x
#             if i % x == 0:
#                 return False

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
