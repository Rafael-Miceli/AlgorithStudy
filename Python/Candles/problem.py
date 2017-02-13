def candles(candles_number, make_new):
    
    leftovers = candles_number

    while leftovers >= make_new:
        leftovers -= make_new
        leftovers += 1
        candles_number += 1

    return candles_number

def candles_2(candles_number, make_new):
    return candles_number + int((candles_number - 1) / (make_new - 1))