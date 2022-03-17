import numpy


def is_prime(n):
    assert n >= 0, "inteiro não positivo"
    if n % 2 == 0 or n == 1:
        return False
    
    for i in range(int(numpy.sqrt(n)/2)):
        if n % (2*i + 3) == 0:
            return False
        else:
            continue
    
    return True
