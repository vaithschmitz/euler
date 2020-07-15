triplet = []
a, b, c = 1, 2, 3
x =  0
while x < 1000:
    a+=1
    b+=1
    c+=1
    x = a + b + c
else: 
    triplet.append([a, b, c])
    print(triplet)
    print(isinstance(a, int))

