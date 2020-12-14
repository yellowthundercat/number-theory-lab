# calculate: a^m % n, m >= 0
def repeated_squaring(a, m, n):
    if m == 0:
        return 1
    result = repeated_squaring(a, m // 2, n)
    if m % 2 == 0:
        return (result * result) % n
    else:
        return (((result * result) % n) * a) % n

def unit_test_repeated_squaring():
    # 2^5 % 7 = 4
    assert repeated_squaring(2, 5, 7) == 4, 'Wrong answer'
    # 2018^2019 % 100 = 32
    assert repeated_squaring(2018, 2019, 100) == 32, 'Wrong answer'
    # 20182019^20192018 % 12345 = 9601
    assert repeated_squaring(20182019, 20192018, 12345) == 9601, 'Wrong answer'
    print('pass unit test')


unit_test_repeated_squaring()

# replace input here
answer = repeated_squaring(3, 5, 7)
print(answer)
