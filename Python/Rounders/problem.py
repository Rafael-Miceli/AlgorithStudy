def rounders(value):            

    zeros = 1
    while value > 10:            
        if value % 10 == 0:
            value = int(value / 10)
            continue
        if value % 10 >= 5:
            value = int(value / 10)
            value += 1
            zeros *= 10
            continue
        
        value = int(value / 10)
        zeros *= 10

    return value * zeros

    
    # gt_5 = value > 9 and value % 10 >= 5
    # zeros = 1

    # while value > 10:            

    #     if value % 10 == 0:
    #         value = int(value / 10)
    #         continue

    #     value = int(value / 10)
    #     zeros *= 10

    # value = value + 1 if gt_5 else value

    # return value * zeros
        