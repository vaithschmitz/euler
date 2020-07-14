def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False

def highprime(x):
    primes = []
    n = 2
    while len(primes) < x:
        if is_prime(n):
            primes.append(n)
        n+=1
    print(primes[x-1])

highprime(10001)