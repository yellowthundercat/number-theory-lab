import math
def extendedEuclid(a,b):
    result=[]
    x1=0
    y1=1
    x2=1
    y2=0
    x=1
    y=0
    while b!=0:
        q=a//b
        r=a%b
        x=x2-q*x1
        y=y2-q*y1
        x2=x1
        y2=y1
        x1=x
        y1=y
        a=b
        b=r
    result.append(a)
    result.append(x2)
    result.append(y2)
    return result
def unit_test():
    # 123456789x + 97654321y =gcd(123456789,97654321) => x=-325154 y=411067 (a,b)=1
    assert  extendedEuclid(123456789,97654321)==[1,-325154,411067],'wrong answer'
    # 37x + 2019y = gcd(37,2019) => x= 382 y=-1 (a,b)=1
    # x= 382 is the modular inverse of 37 mode 2019
    assert extendedEuclid(37, 2019) == [1, 382, -7], 'wrong answer'
    # 37^2 x + 2019^2 y = (37^2,2019^2) => x=735472 y=-247  (a,b)=1
    # x= 735472 is the modular inverse of 37^2 mode 2019^2
    assert extendedEuclid(37**2, 2019**2) == [1, 735472, -247], 'wrong answer'
    print('pass unit test')


unit_test()
answer=extendedEuclid(37,2019)
inverse=answer[1]
print(inverse)
