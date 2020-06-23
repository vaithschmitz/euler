def sum_fibs():
    sum = 0
    x = 1
    y = 0

    while x < 4000000:
        x += y
        y = x -y
        if x % 2 == 0: sum+= x  
    print(sum)

sum_fibs()