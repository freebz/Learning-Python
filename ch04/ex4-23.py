# 그 외의 코어 타입

X = set('spam')                 # 2.X와 3.X에서 순서에 상관없는 집합 만들기
Y = {'h', 'a', 'm'}             # 3.X와 2.7에서 집합 리터럴로 집합 만들기

X, Y                            # 괄호 없는 두 개의 집합으로 된 튜플
# ({'p', 'm', 'a', 's'}, {'m', 'a', 'h'})

X & Y                           # 교집합
# {'m', 'a'}
X | Y                           # 합집합
# {'a', 'p', 'm', 'h', 's'}
X - Y                           # 차집합
# {'p', 's'}
X > Y                           # 상위 집합
# False

{n ** 2 for n in [1, 2, 3, 4]}  # 3.X와 2.7에서 집합 컴프리헨션
# {16, 1, 4, 9}


list(set([1, 2, 1, 3, 1]))      # 중복 제거(아마도 재정렬된다)
# [1, 2, 3]
set('spam') - set('ham')        # 두 컬렉션의 차이
# {'p', 's'}
set('spam') == set('asmp')      # 순서에 상관없이 비교('spam'=='asmp'은 False)
# True


'p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham']
# (True, True, True)



1 / 3                           # 부동 소수점(파이썬 2.X에서 .0 추가)
# 0.3333333333333333
(2/3) + (1/2)
# 1.1666666666666665

import decimal                  # 소수: 고정 정밀도
d = decimal.Decimal('3.141')
d + 1
# Decimal('4.141')

decimal.getcontext().prec = 2
decimal.Decimal('1.00') / decimal.Decimal('3.00')
# Decimal('0.33')

from fractions import Fraction  # 분수: 분자 + 분모
f = Fraction(2, 3)
f + 1
# Fraction(5, 3)
f + Fraction(1, 2)
# Fraction(7, 6)



1 > 2, 1 < 2                    # 부울
# (False, True)
bool('spam')                    # 객체의 부울 값
# True

X = None                        # None
print(X)
# None
L = [None] * 100                # 리스트를 100개의 None으로 초기화
L
# [None, None, None, None, None, None, None, None, None, None, None, None,
# None, None, None, None, None, None, None, None, ...100개의 None 리스트...]
