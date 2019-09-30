# 예제: 제약 조건(하지만 오류는 아닌) 검출하기

def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2

# python
import asserter
asserter.f(1)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File ".\asserter.py", line 2, in f
#     assert x < 0, 'x must be negative'
# AssertionError: x must be negative


def reciprocal(x):
    assert x != 0               # 이런 assert는 일반적으로 불필요함!
    return 1 / x                # 파이썬이 자동으로 0으로 나누는지 여부를 확인함
