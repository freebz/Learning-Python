#!python
# -*- coding: utf-8 -*-
"""
reloadall.py: 이행적으로 중첩된 모듈들을 리로드(2.X +3.X)
하나 또는 그 이상의 임포트된 모듈 객체로 reload_all을 호출할 것
"""

import types
from imp import reload          # 3.X에서 from은 필수

def status(module):
    print('reloading ' + module.__name__)

def tryreload(module):
    try:
        reload(module)          # 3.6(에서만?) 일부 플랫폼에서 실패
    except:
        print('FAILED: %s' % module)

def transitive_reload(module, visited):
    if not module in visited:   # 순환 구조. 중복 잡아내기
        status(module)          # 이 모듈을 리로드
        tryreload(module)       # 그리고 그 자손을 방문
        visited[module] = True
        for attrobj in module.__dict__.values():   # 모든 속성에 대해
            if type(attrobj) == types.ModuleType:  # 만약 모듈이면 재귀적으로 실행
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}                # 진입점
    for arg in args:            # 전달된 모든 인수에 대해
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

def tester(reloader, modname):  # 셀프 테스트 코드
    import importlib, sys       # 테스트에서만 임포트
    if len(sys.argv) > 1: modname = sys.argv[1]   # 명령 라인(또는 통과)
    module = importlib.import_module(modname)     # 이름 문자열로 임포트
    reloader(module)                              # 전달된 리로더(reloader) 테스트

if __name__ == '__main__':
    tester(reload_all, 'reloadall')               # 테스트: 나 자신을 리로드하기?
