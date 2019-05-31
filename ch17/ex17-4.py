# 내장된 이름 재정의하기

def hider():
    open = 'spam'               # 지역 변수. 여기서 내장된 이름은 감춰짐
    ...
    open('data.txt')            # 에러: 이 범위에서는 open으로 파일을 열 수 없음


open = 99                       # 전역 범위에 할당. 여기에서도 내장된 이름은 가려짐


len(dir(builtins)), len([x for x in dir(builtins) if not x.startswith('_')])
# (148, 142)


X = 88                          # 전역 X

def func():
    X = 99                      # 지역 X: 전역은 감추었으나 원하는 것은 전역임

func()
print(X)                        # 88을 출력: 변경 없음
