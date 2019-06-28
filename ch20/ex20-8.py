# 확장된 제너레이터 함수 프로토콜: send vs next

def gen():
    for i in range(10):
        X = yield i
        print(X)

G = gen()
next(G)                         # 제너레이터를 시작하기 위해 먼저 next() 호출해야 함
# 0
G.send(77)                      # 다음 값으로 이동. 그리고 값을 yield 표현식으로 보냄
# 77
# 1
G.send(88)
# 88
# 2
next(G)                         # next()와 X.__next()는 None을 보냄
# None
# 3
