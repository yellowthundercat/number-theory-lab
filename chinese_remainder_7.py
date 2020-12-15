def findU(a, n):
    """
        Find the solution z of the congruence az = 1 (mod n),
        where a, n, z is integers, z is positive.

        Inputs a, n.

        Outputs z.
    """
    
    # Initialize z as 0 and increase z and test until az = 1 (mod n):

    z = 0
    while (True):
        z += 1
        if (a*z) % n == 1:
            return z


def solveSystemOfCongruences(N, A): 
    """
        Find the solution x of system of congruences by Chinese Remainder Theorem.

        Inputs two list N and A, 
        where N = [n_1, n_2, ..., n_k], A = [a_1, a_2, ..., a_k] 
        with (n_i, n_j) with i!=j is pairwise relatively prime of positive integers, 
        a_i is abitrary integers such that,

        x = a_1 (mod n_1)
        x = a_2 (mod n_2)
        ...
        x = a_k (mod n_k)

        Returns x.
    """
    
    # Apply Chinese Remainder Theorem
    # The integer y is the solution to the system if and only if x = y (mod n_1...n_k)
    
    # Find production = n_1...n_k:
    production = 1
    y = 0
    for n in N:
        production *= n  # production = production * n_i for all i

    for i in range(0, len(N)):
        _n = production / N[i]
        y += A[i] * _n * findU(_n, N[i]) # y = y + a_i*_n*z such that az = 1 (mod n_i) for all i
    return y % production # x = y (mod production)
