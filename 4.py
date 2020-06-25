def largest_palindrome_product(n):
    res = 0
    out = []
    i = n

    # outer dec loop through n
    while i >= 1:
        # full run of inner decrementing loop (n, 1) for each outer n
        while n >= 1 and i != 1:
            # multiple outer n and inner n
            res = i*n
            # if palindrome add to list
            if list(map(int, str(res))) == list(map(int, str(res)))[::-1]:
                out.append(res)
            n -=1
        n = 999
        i-=1
    print(sorted(out)[-1])



largest_palindrome_product(999)
