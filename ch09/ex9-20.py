# 파이썬의 타입 계층 구조

# 타입 객체

type([1]) == type([])           # 서로 다른 리스트의 타입 비교
type([1]) == list               # 리스트 타입 이름의 비교
isinstance([1], list)           # 객체의 타입 확인

import types                    # types는 다른 타입들을 위한 이름을 제공
def f(): pass
type(f) == types.FunctionType
