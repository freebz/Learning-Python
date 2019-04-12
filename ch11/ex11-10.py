# 증강 할당과 공유 참조

L = [1, 2]
M = L                           # L과 M은 같은 객체를 참조함
L = L + [3, 4]                  # 연결은 새로운 객체를 만듦
L, M                            # L만 변경됨
# ([1, 2, 3, 4], [1, 2])


L = [1, 2]
M = L
L += [3, 4]                     # 그러나 +=는 실제로 extend를 의미함
L, M
# ([1, 2, 3, 4], [1, 2, 3, 4])
