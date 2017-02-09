def increaseNumberRoundness(n):
    while n % 10 == 0:
        n = int(n / 10)

    while len(str(n)) > 1 :
        if n % 10 == 0:
            return True    
        n = int(n / 10)

    return False