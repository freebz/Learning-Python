# 고급 시퀀스 할당 패턴

string = 'SPAM'
a, b, c, d = string             # 양쪽에 같은 수의 항목
a, d
# ('S', 'M')

a, b, c, = string               # 그렇지 않은 경우 에러 발생
# ...에러 텍스트 생략...
# ValueError: too many values to unpack (expected 3)


a, b, c = string[0], string[1], string[2:] # 인덱스와 슬라이스
a, b, c
# ('S', 'P', 'AM')

a, b, c = list(string[:2]) + [string[2:]] # 슬라이스와 연결
a, b, c
# ('S', 'P', 'AM')

a, b = string[:2]               # 위와 같지만 좀 더 단순한 방법
c = string[2:]
a, b, c
# ('S', 'P', 'AM')

(a, b), c = string[:2], string[2:] # 중첩된 시퀀스
a, b, c
# ('S', 'P', 'AM')


((a, b), c) = ('SP', 'AM')      # 형태와 위치에 따라 짝지어짐
a, b, c
# ('S', 'P', 'AM')


for (a, b, c) in [(1, 2, 3), (4, 5, 6)]: ... # 단순한 튜플 할당

for ((a, b), c) in [((1, 2), 3), ((4, 5), 6)]: ... # 중첩된 튜플 할당



def f(((a, b), c)): ...         # 파이썬 2.X(3.X 제외)에서 인수에 대해서도 동작함
f(((1, 2), 3))


red, green, blue = range(3)
red, blue
# (0, 2)


list(range(3))                  # list()는 파이썬 3.X에서만 필요
# [0, 1, 2]


L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]      # 3.X에서 *을 이용하는 방법은 다음 절 참조
    print(front, L)

# 1 [2, 3, 4]
# 2 [3, 4]
# 3 [4]
# 4 []


    front = L[0]
    L = L[1:]
