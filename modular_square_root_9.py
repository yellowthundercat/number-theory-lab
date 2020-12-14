# find generator and log
from helper.find_factorization import find_factorization
import random
from repeated_squaring_1 import 

# find generator of Z*p
# input: prime
# output: integer
def find_generator(p):
    factor = find_factorization(p - 1)
    random.seed(1)
    for prime, expo in factor:
        beta = 1
        while beta == 1:
            alpha = random.randint(2, p-1)



