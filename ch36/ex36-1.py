# 중첩 예외 핸들러

# 예제: 제어 흐름 중첩

def action2():
    print(1 + [])               # 타입 오류를 생성

def action1():
    try:
        action2()
    except TypeError:           # 가장 최근 것 중 맞는 try문
        print('inner try')

try:
    action1()
except TypeError:               # 여기, action1이 다시 일어날 때만
    print('outer tyr')

# python nextexc.py
# inner try
