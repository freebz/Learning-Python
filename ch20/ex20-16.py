# 제너레이터와 라이브러리 도구: 디렉터리 탐색기

import os
for (root, subs, files) in os.walk('.'): # 디렉터리 탐색기 제너레이터
    for name in files:                   # 파이썬 'find' 기능
        if name.startswith('call'):
            print(root, name)

# . callables.py
# .\dualpkg callables.py


G = os.walk(r'C:\code\pkg')
iter(G) is G                    # 일회용 탐색 반복자: iter(G)는 필수 아님
# True
I = iter(G)
next(I)
# ('C:\\code\\pkg', ['__pycache__'], ['eggs.py', 'eggs.pyc', 'main.py', ...등등...])
next(I)
# ('C:\\code\\pkg\\__pycache__', [], ['eggs.cpython-36.pyc', ...등등...])
next(I)
# StopIteration
