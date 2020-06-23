def multiples(): 
    nums = set()
    x = 1
    while x < 1000:
        if (x % 3 == 0) or (x % 5 == 0):
            nums.add(x)
        x+=1
    print(sum(nums))

multiples()

