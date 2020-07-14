def sumsquarediff(i):
    nums = list(range(1, i+1))
    sumsquares = 0
    squaresum = 0
    for num in nums: 
        sumsquares += num*num
    
    listsum = 0
    for num in nums:
        listsum += num
    squaresum = listsum * listsum



    print(squaresum - sumsquares)

sumsquarediff(100)