# 표현식문과 직접 변경

L = [1, 2]
L.append(3)                     # append는 리스트를 직접 변경함
L
# [1, 2, 3]


L = L.append(4)                 # 그러나 append는 L이 아닌 None을 반환함
print(L)                        # 그래서 리스트를 잃게 됨
# None
