# 튜플

T = (1, 2, 3, 4)                # 네 개의 아이템으로 구성된 튜플
len(T)                          # 튜플의 길이
# 4

T + (5, 6)                      # 연결
# (1, 2, 3, 4, 5, 6)

T[0]                            # 인덱싱, 슬라이스 등
# 1



T.index(4)                      # 튜플 메서드: 4는 오프셋 3에 위치함
# 3
T.count(4)                      # 튜플 안에 4가 한 번 나타남
# 1


T[2] = 2                        # 튜플은 변경할 수 없음
# ...에러 텍스트 생략...
# TypeError: 'tuple' object does not support item assignment

T = (2,) + T[1:]                # 새로운 값을 위한 새로운 튜플 생성
# (2, 2, 3, 4)


T = 'spam', 3.0, [11, 22, 33]
T[1]
# 3.0
T[2][1]
# 22
T.append(4)
# AttributeError: 'tuple' object has no attribute 'append'
