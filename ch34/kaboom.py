# -*- coding: utf-8 -*-
def kaboom(x, y):
    print(x + y)                # TypeError를 발생시킴

try:
    kaboom([0, 1, 2], 'spam')
except TypeError:               # 여기서 예외를 캐치하고 복구
    print('Hello world!')
print('resuming here')          # 예외 발생 여부와 상관없이 이 코드를 실행
