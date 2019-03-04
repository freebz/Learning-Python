# 분수 변환과 혼합 타입

(2.5).as_integer_ratio()            # 부동 소수점 수 객체 메서드
# (5, 2)

f = 2.5
z = Fraction(*f.as_integer_ratio()) # 부동 소수점 수 -> 분수 변환: 두 개의 인수로 변환
z                                   # Fraction(5, 2)와 같다
# Fraction(5, 2)

x                                   # 이전 절에서 설정된 x
# Fraction(1, 3)
x + z
# Fraction(17, 6)                   # 5/2 +1/3 = 15/6 + 2/6

float(x)                            # 분수 -> 부동 소수점 수로 변환
# 0.3333333333333333
float(z)
# 2.5
float(x + z)
# 2.8333333333333335
17 / 6
# 2.8333333333333335

Fraction.from_float(1.75)           # 부동 소수점 수 -> 분수 변환: 다른 방법
# Fraction(7, 4)


x
# Fraction(1, 3)
x + 2                           # 분수 + 정수 -> 분수
# Fraction(7, 3)
x + 2.0                         # 분수 + 부동 소수점 수 -> 부동 소수점 수
# 2.3333333333333335
x + (1./3)                      # 분수 + 부동 소수점 수 -> 부동 소수점 수
# 0.6666666666666666
x + (4./3)
# 1.6666666666666665
x + Fraction(4, 3)              # 분수 + 분수 -> 분수
# Fraction(5, 3)


4.0 / 3
# 1.3333333333333333
(4.0 / 3).as_integer_ratio()    # 부동 소수점 수로부터 정밀도 손실
# (6004799503160661, 4503599627370496)

x
# Fraction(1, 3)
a = x + Fraction(*(4.0 / 3).as_integer_ratio())
a
# Fraction(22517998136852479, 13510798882111488)

22517998136852479 / 13510798882111488.          # 5/3(또는 근접함!)
# 1.6666666666666667

a.limit_denominator(10)                         # 가장 근접한 분수로 단순화
# Fraction(5, 3)