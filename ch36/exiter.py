import sys
def bye():
    sys.exit(40)                # 결정적인 에러: 바로 종료할 것!
try:
    bye()
except:
    print('got it')             # 아차차, 프로그램은 종료하지 말 것
print('continuing...')
