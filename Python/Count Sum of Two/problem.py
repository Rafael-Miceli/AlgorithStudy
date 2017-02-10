def my_sum(n, l, r):
    tot = 0
    for num in range(l, r + 1):        
        for nu in range(num, r + 1):
            if num + nu == n:
                tot += 1
    return tot

def my_sum_2(n, l, r):          
    result = min((n/2 - l + 1), (r - n/2 + 1))    
    return 0 if result < 0 else int(result)

def my_sum_3(n, l, r):
    tot = 0
    for num in range(l, r + 1):                
        if num <= n - num <= r:
            tot += 1
    return tot