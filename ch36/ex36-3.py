# 예외 어법

# 다중 중첩 루프에서 벗어나기: 'go to'

class Exitloop(Exception): pass

try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise Exitloop    # 한 레벨만 벗어남
                print('loop3: %s' % i)
            print('loop2')
        print('loop1')
except Exitloop:
    print('continuing')                     # 또는 그냥 지나가고 계속 진행함

# loop3: 0
# loop3: 1
# loop3: 2
# loop3: 3
# continuing
i
# 4
