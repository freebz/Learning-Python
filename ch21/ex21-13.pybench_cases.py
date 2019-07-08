"""
pybench_cases.py: 일련의 파이썬과 문들에 대해 pybench를 실행함

이 스크립트를 수정하거나 또는 명령 라인 인수를 사용하여 모드를 선택해 보자.
예를 들어, 'C:\python27\python pybench_cases.py'를 실행하여 파이썬 한 버전에 대해 여러 문을 실행하거나,
'pybench_cases.py -a'를 실행하여 나열된 모든 파이썬 버전에 대해 테스트하거나, 'py -3 pybench_cases.py -a -t'
실행하여 명령 라인을 추적할 수 있다.
"""

import pybench, sys

pythons = [                         # (버전 3인지, 경로)
    (1, 'C:\python36\python'),
    (0, 'C:\python27\python'),
    (0, 'C:\pypy\pypy-1.9\pypy')
]

stmts = [                                       # (실행 횟수, 반복 횟수, 문)
    (0, 0, "[x ** 2 for x in range(1000)]"),    # 반복
    (0, 0, "res=p]\nfor x in range(1000): res.append(x ** 2)"),    # \n = 여러 문을
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),        # \n\t = 들여쓰기
    (0, 0, "list(x ** 2 for x in range(1000))"),                   # $ = list 또는 "
    (0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"), # 문자열 연산
    (0, 0, "s = '?'\nfor i in range(10000): s += '?'"),
]

tracemd = '-t' in sys.argv                         # -t: 명령 라인 추적
pythons = pythons if '-a' in sys.argv else None    # -a: 사용할 파이썬
pybench.runner(stmts, pythons, tracemd)
