# 파이썬 2.X에서의 슬라이싱과 인덱싱

# py -2
class Slicer:
    def __getitem__(self, index):      print index
    def __getslice__(self, i, j):      print i, j
    def __setslice__(self, i, j, seq): print i, j, seq

Slicer()[1]                     # 3.X처럼 __getitem__을 정수와 함께 실행
# 1
Slicer()[1:9]                   # 만약 존재하면 __getslice__, 아니면 __getitem__
# 1 9
Slicer()[1:9:2]                 # 3.X처럼 __getitem__을 slice()로 실행
# slice(1, 9, 2)
