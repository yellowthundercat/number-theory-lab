
def findU(z, n):
    u = 0
    while (True):
        if (u*z) % n == 1:
            return u
        u += 1 

def findX(N, A):
    production = 1
    y = 0
    for n in N:
        production *= n  
    for i in range(0, len(N)):
        _n = production / N[i]
        y += A[i] * _n * findU(_n, N[i])
    return y % production


N = [27, 20]
A = [15, 16]
print(findX(N, A))