# 순환 데이터 구조에 주의하라

L = ['grail']                   # 동일한 객체의 대한 참조를 추가함으로써
L.append(L)                     # 객체 안에 순환을 만듦: [...]
L
# ['grail', [...]]
