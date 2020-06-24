def largest_palindrome_product(n):
    res = 0
    out = 0
    j = 1
    i = n
    while n >= i:
        res  = n * i
        print(i)
        print(n)
        # if palindrome, write to list
        if list(map(int, str(res))) == list(map(int, str(res)))[::-1]:
            out = res 
            
        if n == i:
            while n >= j:
                res  = n * j  
                if list(map(int, str(res))) == list(map(int, str(res)))[::-1]:
                    out = res 
                    j -=1
                else: 
                    j-=1
        n-=1

    print(out)

    # dec in reverse, kill after first check



largest_palindrome_product(999)
