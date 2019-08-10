# -*- coding: utf-8 -*-
"""
reloadall3.py: 중첩된 모듈들을 이행적으로 리로드(명시적 스택)
"""

import types
from imp import reload          # from은 3.X에서는 필수
from reloadall import status, tryreload, tester

def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()    # 끝에서 next 항목 삭제
        status(next)            # 이것을 리로드, 속성 밀어 넣기
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values()
            if type(x) == types.ModuleType and x not in visited)

def reload_all(*modules):
    transitive_reload(list(modules), set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall3') # 테스트 코드: 나 자신을 리로드?
