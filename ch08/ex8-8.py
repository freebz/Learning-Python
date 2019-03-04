# 또 다른 리스트 연산

L = ['spam', 'eggs', 'ham', 'toast']
del L[0]                        # 아이템 하나 삭제
L
# ['eggs', 'ham', 'toast']
del L[1:]                       # 전체 섹션 삭제
L
# ['eggs']


L = ['Already', 'got', 'one']
L[1:] = []
L
# ['Already']
L[0] = []
L
# [[]]
