def apple_boxes(k):
    yellow_apples = 0
    red_apples = 0

    for num in range(k + 1):
        if num & 1 == 0:
            red_apples += (num * num)
        else:
            yellow_apples += (num * num)
    
    return red_apples - yellow_apples

def apple_boxes_deterministically(k):
    return k * (k + 1) / (2 if k & 1 == 0 else -2)