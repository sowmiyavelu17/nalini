def sumOdd(n):
    for i in range(n):
        if n%2==0:  # if n is odd
            n -= 1
            print(sum(range(1,n,2))+ n) 
sumOdd(123)  # 4
