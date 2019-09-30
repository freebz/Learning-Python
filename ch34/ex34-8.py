# 예외: try/finally를 이용해 종료 동작 코드 작성하기

class MyError(Exception): pass

def stuff(file):
    raise MyError()

file = open('data', 'w')        # 출력 파일을 염(이 동작도 실패할 수 있음)

try:
    stuff(file)                 # 예외를 발생시킴
finally:
    file.close()                # 출력 버퍼를 비우기 위해 항상 파일을 닫음
print('not reached')            # 이 코드는 예외가 발생하지 않았을 때만 실행됨
