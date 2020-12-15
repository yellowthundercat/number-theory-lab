from repeated_squaring_1 import repeated_squaring
from euclidean_extended_4 import extendedEuclid
import math


def modular_sqrt_prime(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return 0
    elif p % 4 == 3:
        return repeated_squaring(a, (p + 1) / 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = repeated_squaring(a, (s + 1) / 2, p)
    b = repeated_squaring(a, s, p)
    g = repeated_squaring(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = repeated_squaring(t, 2, p)

        if m == 0:
            return x

        gs = repeated_squaring(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = repeated_squaring(a, (p - 1) / 2, p)
    return -1 if ls == p - 1 else ls


# find result^2 = a (mod p^e)
def modular_sqrt_prime_power(a, p, e):
    result = modular_sqrt_prime(a, p)
    current_prime_power = p
    for i in range(1, e):
        previous_prime_power = current_prime_power
        current_prime_power *= p
        inverse_mod = extendedEuclid(2*result, p)[1]
        h = inverse_mod * ((a - (result**2)) // previous_prime_power)
        h %= current_prime_power
        result = result + (previous_prime_power * h)
        result %= current_prime_power
    return result

def unit_test():
    # test prime
    assert (modular_sqrt_prime(13290059, 127)**2) % 127 == 13290059 % 127, 'wrong find modular square root prime'
    # test prime power
    assert (modular_sqrt_prime_power(13290059, 127, 5)**2) % (127**5) == 13290059 % (127**5), \
        'wrong find modular square root prime power'

    print('pass unit test modular square root')


unit_test()

print(modular_sqrt_prime(13290059, 127))
print(modular_sqrt_prime_power(13290059, 127, 2))
