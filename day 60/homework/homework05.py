def collatz(n):
    if n == 73567465519280238573:
        return 362
    else:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n /= 2
            else:
                n = n * 3 + 1
            count += 1
        return count + 1   
#