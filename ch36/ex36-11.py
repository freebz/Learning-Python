# 예외 설계 팁과 주의 사항

# 무엇을 감쌀 것인가

# 너무 많이 잡아낸다는 것: 빈 except와 Exception을 피할 것

def func():
    try:
        ...                     # IndexError가 여기에서 발생
    except:
        ...                     # 하지만 모든 것은 여기로 와서 죽는다!

try:
    func()
except IndexError:              # 예외는 여기에서 처리되어야 함
    ...


import sys
def bye():
    sys.exit(40)                # 결정적인 에러: 바로 종료할 것!
try:
    bye()
except:
    print('got it')             # 아차차, 프로그램은 종료하지 말 것
print('continuing...')

    
# python exiter.py 
# got it
# continuing...


try:
    bye()
except Exception:               # 종료를 잡아내지는 않지만, 그외 많은 것들을 잡아냄
    ...


mydictionary = {...}
...
try:
    x = myditctionary['spam']   # 아차: 철자를 잘못 썼군
except:
    x = None                    # 우리가 KeyError를 받을 거라고 가정함
...x를 계속 사용함...
