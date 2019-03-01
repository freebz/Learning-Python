# 문자열 변환 도구

# 파이썬 3.X
"42" + 1
# TypeError: Can't convert 'int' object to str implicitly

# 파이썬 2.X
"42" + 1
# TypeError: cannot concatenate 'str' and 'int' objects


int("42"), str(42)              # 문자열에서 숫자로, 숫자에서 문자열로 변환
# (42, '42')
repr(42)                        # 코드 문자열로 변환
# '42'


print(str('spam'), repr('spam')) # 2.X: print str('spam'), repr('spam')
# spam 'spam'
str('spam'), repr('spam')       # 원시 대화형 출력
# ('spam', "'spam'")


S = "42"
I = 1
S + I
# TypeError: Can't convert 'int' object to str implicitly

int(S) + I                      # 강제로 더하기
# 43

S + str(I)                      # 강제로 연결하기
# '421'


str(3.1415), float("1.5")
# ('3.1415', 1.5)

text = "1.234E-10"
float(text)                     # 2.7과 3.1 이전에는 더 많은 자릿수가 출력됨
# 1.234e-10
