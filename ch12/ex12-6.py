# 몇몇 특별한 경우

L = ["Good",
     "Bad",
     "Ugly"]                    # 열린 구문 쌍 규칙을 이용한 라인 확장


if a == b and c == d and  \
   d == e and f == g:
    print('old')                # 역 슬래시는 연속 라인 입력을 가능하게 함


if (a == b and c == d and
    d == e and e == f):
    print('new')                # 괄호도 같은 역할을 하며, 일반적으로 더 명확함


x = 1 + 2 + 3 \                 # \가 생략될 경우 전혀 다른 결과가 나온다!
+4


x = 1; y = 2; print(x)          # 하나 이상의 비복합문


S = """
aaaa
bbbb
cccc"""

S = ('aaaa'
     'bbbb'                     # 이 주석은 무시됨
     'cccc')


if 1: print('hello')            # 헤더 라인에 포함된 간단한 문
