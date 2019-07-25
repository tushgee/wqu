def mersenne_number(p):
    if p==1: 
        return 1
    return 2*mersenne_number(p-1)


print(mersenne_number(3))