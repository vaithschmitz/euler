def smallest_evenly_div():
    i = 20
    n = 1
    while i >= 1:
        if i == 1:
            print(n)
            return
        elif n % i == 0: 
            i-=1
        else:
            n += 1
            i = 20

smallest_evenly_div()