def findU(z, n):
    u = 0
    while (True):
        if (u*z) % n == 1:
            return u
        u += 1 


#N = [n_1, n_2, n_3, ...], A = [a_1, a_2, a_3, ...]
# findX(N, A) is the solution of the system 
# x = a_1 (mod n_1)
# x = a_2 (mod n_2)
# x = a_3 (mod n_3)
# ...

# Example:
# N = [27, 20]
# A = [15, 16]
# print(findX(N, A))

def findX(N, A): 
    production = 1 # production = n_1 . n_2 . n_3 . ...
    y = 0
    for n in N:
        production *= n  
    for i in range(0, len(N)):
        _n = production / N[i]
        y += A[i] * _n * findU(_n, N[i])
    return y % production

