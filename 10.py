import time

start = time.time()
primes = []

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False

i = 2
res = 0

while i < 2000000:
    if i % 2 == 0: 
        i += 1
    elif is_prime(i):
        primes.append(i)
        i +=1
    else:
        i+=1
    print(primes)
    

for j in primes:
    res += j
print(f'res: {res}')
end = time.time()
duration = end -start

print(f'time: {duration}')