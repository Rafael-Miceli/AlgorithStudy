
#indicies = reversed(range(len(elements)))
#for i, element in zip(indicies, elements):
#code

# 456
#1734
def add_without_care(param1, param2):

    maior = param1 if param1 > param2 else param2
    menor = param1 if param1 < param2 else param2
    maior_str = str(maior)
    menor_str = str(menor)
    str_tot = ''

    cont = 1
    for i, val_1 in reversed(list(enumerate(maior_str))):                        

        val = int(val_1)

        if len(menor_str) >= cont:
            val = int(menor_str[len(menor_str) - cont]) + int(val_1) 

        if val > 9:
            val = val % 10
        
        str_tot += str(val)
        cont += 1


    return int(str_tot[::-1])


def add_without_care_2(p1, p2):
    if p1 != 0 or p2!=0:
            t = ''
            while p1 > 0 or p2 > 0:
                t = str((p1%10+p2%10)%10) + t
                p1 /= 10
                p2 /= 10
            return int(t)
    return 0