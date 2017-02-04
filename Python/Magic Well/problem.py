def castwell(a, b, n):

    tot = 0
    for num in range(n):
        tot += a * b
        a += 1
        b += 1

    return tot

def castwell_2(a, b, n):
    if not n:
        return 0
    
    return a*b + castwell_2(a+1,b+1,n-1)