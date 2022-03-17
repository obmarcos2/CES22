import numpy


def is_prime(n):
    if n % 2 == 0:
        return False
    
    for i in range(int(numpy.sqrt(n)/2)):
        if n % (2*i + 3) == 0:
            return False
        else:
            continue
    
    return True
