#cacalate m such that m^2 + 1 = 0 mod p (p prime number of the form 4k+1)

def pow(a,b,m):
    result=1
    a%=m
    while b>0:
        if b%2==1:
            result=(result*a)%m
        b//=2
        a=(a*a)%m
    return result
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)


def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1<<(m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r


n=448
p=673
r = tonelli(n, p)
print("n = %d p = %d" % (n, p))
print("\t  roots : %d %d" % (r, p - r))
# m = 992 or m =1037
print(((r)**2)%p)
# test 1037^2 + 1 = 0 mod 2029
