def smallest_evenly_div():
    i = 1
    n = 1
    while i <= 20:
        if n % i == 0: 
            print(n)
            i+=1
        elif i == 20:
            print(n)
            return
        else:
            n += 1
            i = 1
            print(n)

smallest_evenly_div()