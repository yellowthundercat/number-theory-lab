def factorize(a): 
    """
        Factorize a into a = 2^h * b such that h is maximum as possible.

        Returns h, b.
    """
    h = 0
    b = a
    while b % 2 == 0:
        b = b >> 1
        h += 1
    return h, b

def jacobiCompute(a, n): 
    """
        Compute Jacobi symbol (a | n)
        where a is integer, n is positive and odd integer 
        such that n = q_1...q_k with q_i are odd primes and not neccessary distinct.

        Return 0 if n divides a, 
        1 if n does not divide a and a is a quadratic residue modulo n,
        -1 if n does not divide a and a is a quadratic nonresidue modulo n.
    """
    alpha = 1
    while (True):
        a = a % n
        if a == 0:
            if n == 1:
                return alpha
            return 0
        h, b = factorize(a)
        if (h % 2 != 0) and (n % 8 != 1) and (n % 8 != -1):
            alpha = -alpha
        if (b % 4 != 1) and (n % 4 != 1):
            alpha = -alpha
        a = n
        n = b
        
