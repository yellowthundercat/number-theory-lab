# find generator and log
from helper.find_factorization import find_factorization
import random
from repeated_squaring_1 import repeated_squaring
import math

# find generator of Z*p
# input: prime
# output: integer
def find_generator(p):
    factor = find_factorization(p - 1)
    random.seed(1)
    result = 1
    for prime, expo in factor:
        beta = 1
        alpha = 0
        while beta == 1:
            alpha = random.randint(2, p-1)
            beta = repeated_squaring(alpha, (p-1)/prime, p)
        result *= repeated_squaring(alpha, (p-1)/(prime**expo), p)
        result = result % p
    return result

# input: generator, alpha, prime p
# output: k whether generator^k = alpha mod p
def find_log(generator, alpha, p):
    N = math.ceil(math.sqrt(p - 1))  # phi(p) is p-1 if p is prime

    # Store hashmap of g^{1...m} (mod p). Baby step.
    tbl = {repeated_squaring(generator, i, p): i for i in range(N)}

    # Precompute via Fermat's Little Theorem
    c = repeated_squaring(generator, N * (p - 2), p)

    # Search for an equivalence in the table. Giant step.
    for j in range(N):
        y = (alpha * repeated_squaring(c, j, p)) % p
        if y in tbl:
            return j * N + tbl[y]

    # Solution not found
    return None

def find_log_bruteforce(generator, alpha, p):
    beta = 1
    i = 0
    while beta != alpha:
        beta = (beta * generator) % p
        i += 1
    return i


def check_generator(prime, generator):
    exist_set = set()
    new_number = 1
    for i in range(1, prime):
        new_number *= generator
        new_number = new_number % prime
        if new_number in exist_set:
            return False
        exist_set.add(new_number)
    return True

def unit_test():
    # test generator
    assert check_generator(3, find_generator(3)), 'wrong generator'
    assert check_generator(524287, find_generator(524287)), 'wrong generator'
    # test log
    assert find_log(7894352216, 355407489, 604604729) == 102900819, 'wrong find log'
    assert find_log(find_generator(524287), 3, 524287) == find_log_bruteforce(find_generator(524287), 3, 524287), \
        'wrong find log'

    print('pass unit test generator and log')


unit_test()

y_generator = find_generator(13)
answer_log = find_log(y_generator, 5, 13)
print(y_generator)
print(answer_log)
