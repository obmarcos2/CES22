import numpy


def is_prime(n):
    for i in range(int(numpy.sqrt(n))):
        if n % (i + 2) == 0:
            return False
        else:
            continue
    return True
