# 기본값과 가변 객체

def saver(x=[]):                # 빈 리스트 객체를 저장함
    x.append(1)                 # 동일한 객체를 호출 때마다 변경함
    print(x)

saver([2])                      # 기본값이 사용되지 않음
# [2, 1]
saver()                         # 기본값이 사용됨
# [1]
saver()                         # 호출 때마다 늘어남
# [1, 1]
saver()
# [1, 1, 1]


def saver(x=None):
    if x is None:               # 인수가 전달되지 않았다면?
        x = []                  # 호출될 때마다 새로운 리스트를 만들기 위해 실행
    x.append(1)                 # 새로운 리스트 객체 변경
    print(x)

saver([2])
# [2, 1]
saver()                         # 늘어나지 않음
# [1]
saver()
# [1]


def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []
saver()
# [1]
saver()
# [1, 1]
saver()
# [1, 1, 1]
