# timer0.py 파일
import time
def timer(func, *args):         # 단순한 타이밍 함수
    start = time.clock()
    for i in range(1000):
        func(*args)
    return time.clock() - start # 총 경과 시간(초)
