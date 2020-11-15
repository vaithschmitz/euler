# min val for c == 335 to confirm a<b<c == 1000 
# max val for c == 997
a=1
b=2
c=3
def is_triplet(a,b,c):
    if a**2 + b**2 == c**2:
        print(a*b*c)

for c in range(335, 997):
    for b in range(2, c-b):
        for a in range(2, b-a):
            # print(a,b,c)
            if(a+b+c) ==1000:
                is_triplet(a,b,c)
        if(a+b+c) ==1000:
            is_triplet(a,b,c)
    if(a+b+c) ==1000:
        is_triplet(a,b,c)
    