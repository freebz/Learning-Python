# dir 함수

import sys
dir(sys)
# ['__displayhook__', ...나머지 이름은 생략..., 'winver']



len(dir(sys))                   # sys에 포함된 이름 수
# 78
len([x for x in dir(sys) if not x.startswith('__')]) # __X를 제외한 이름 수
# 69
len([x for x in dir(sys) if not x[0] == '_']) # 언더스코어 문자로 시작하는 이름 제외
# 62


dir([])
# ['__add__', '__class__', '__contains__', ...more..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

dir('')
# ['__add__', '__class__', '__contains__', ...more..., 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


len(dir([])), len([x for x in dir([]) if not x.startswith('__')])
# (45, 11)
len(dir('')), len([x for x in dir('') if not x.startswith('__')])
# (76, 44)


[ a for a in dir(list) if not a.startswith('__')]
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

[a for a in dir(dict) if not a.startswith('__')]
# ['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']


def dir1(x): return [a for a in dir(x) if not a.startswith('__')] # 파트 4 참고

dir1(tuple)
# ['count', 'index']


dir(str) == dir('')             # 타입 이름과 리터럴의 결과가 같음
# True
dir(list) == dir([])
# True
