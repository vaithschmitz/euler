import time

start = time.time()
prime_sum = 0


prime = [True for i in range(1001)] 
p = 2

while p * p <= 1000:
    if prime[p] == True:
        for i in range(p*p, 1001, p):
            prime[i] = False
    p += 1

print(prime)

# print(prime_sum)

    
end = time.time()
duration = end -start
print(prime_sum)
print(f'time: {duration}')