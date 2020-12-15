def gcd(a,b):
    while b!=0:
        remainder=a%b
        a=b
        b=remainder
    return a
def unit_test():
    # gcd(2021019,1431471) = 2019
    assert gcd(2021019,1431471) == 2019, 'Wrong answer'
   # gcd(1234567,234569)= 127
    assert gcd(1234567,234569) == 127, 'Wrong answer'
    # gcd(1234567,56789) = 1
    assert gcd(1234567,56789) == 1, 'Wrong answer'
    print('pass unit test gcd')

unit_test()
answer=gcd(2021019,1431471)
print(answer)

