# 반복과 최적화

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
squares
# [1, 4, 9, 16, 25]


squares = []
for x in [1, 2, 3, 4, 5]:       # 리스트 컴프리헨션이 하는 일
    squares.append(x ** 2)      # 둘 모두 내부적으로 반복 프로토콜을 실행함

squares
# [1, 4, 9, 16, 25]
