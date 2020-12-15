import math

# find factorization
# input: integer
# output: list of prime and exponent (2^3*3^5 = [(2,3), (3,5)])
def find_factorization(k):
    result = []
    i = 2
    square_root_k = math.sqrt(k)
    while i <= square_root_k:
        if k % i == 0:
            expo = 0
            while k % i == 0:
                expo += 1
                k //= i
            result.append((i, expo))
            square_root_k = math.sqrt(k)
        i += 1

    if k > 1:
        result.append((k, 1))
    return result


def unit_test():
    assert str(find_factorization(6804)) == str([(2, 2), (3, 5), (7, 1)]), 'wrong factorize'
    assert str(find_factorization(2473891725321)) == str([(3, 2), (524287, 2)]), 'wrong factorize'
    print('pass unit test factorize')

unit_test()

