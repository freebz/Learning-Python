# 외부 try문을 사용하여 디버깅하기

try:
    ...프로그램 실행...
except:                         # 모든 잡히지 않은 예외는 여기로 모임
    import sys
    print('uncaught!', sys.exc_info()[0], sys.exc_info()[1])
