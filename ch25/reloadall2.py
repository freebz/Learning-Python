# -*- coding: utf-8 -*-
"""
reloadall2.py: 이행적으로 중첩된 모듈들을 리로드(다른 방식의 코딩)
"""

import types
from imp import reload          # from은 3.X에서 필수
from reloadall import status, tryreload, tester

def transitive_reload(objects, visited):
    for obj in objects:
        if type(obj) == types.ModuleType and obj not in visited:
            status(obj)
            tryreload(obj)      # 이것을 리로드, 속성으로 되돌아감
            visited.add(obj)
            transitive_reload(obj.__dict__.values(), visited)

def reload_all(*args):
    transitive_reload(args, set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall2') # 테스트 코드: 나 자신을 리로드?
