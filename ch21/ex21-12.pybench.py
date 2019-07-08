# 벤치마크 모듈과 스크립트: timeit

"""
pybench.py: 간단한 코드 문자열에 대한 하나 또는 여러 파이썬의 속도를 측정하는 벤치마크.
다양한 문들을 허용하는 함수. 이 시스템 자체는 2.X와 3.X 모두에서 실행될 수 있다.

현재 스크립트를 실행하는 파이썬이나, 파이썬 세트를 테스트하기 위해 timeit을 사용하며,
파이썬 세트는 모듈 검색 경로에서 timeit을 찾기 위해 -m 플래그를 사용하여 명령 라인을 통해 실행된다.
3.X에서 실행을 위해 제너레이터를 둘러싼 $listif3을 list()로 대체하며, 3.X의 경우 제너레이터를 둘러싼 $listif3을
list()로 대체하고 2.X의 경우 빈 문자열로 대체하여 3.X에서도 2.X가 동일하게 동작한다.

명령 라인 모드에서 문이 여러 라인인 경우 한 라인에 하나씩 별도로 인용되어야 실행될 수 있기 때문에
멀티라인문을 분할한다(그렇지 않으면 첫 번째 라인만 실행/측정된다). 그리고 들여쓰기에 사용된 모든 \t를
스페이스 네 개로 대체한다.

주의 사항: 명령 라인 모드에서는 테스트 stmt가 이중 인용 부호를 포함할 경우 실패할 수 있으며,
인용된 stmt 문자열은 일반적으로 셀과 호환되지 않거나, 명령 라인은 플랫폼 셸의 길이 제한을 초과할 수 있다.
API 호출 모드나 직접 작성한 타이머를 사용하도록 하자. 아직 설정(setup)문은 지원하지 않는다. 직접 보다시피
테스트 stmt에 있는 모든 문을 실행하는 시간은 전체 시간에 반영된다.
"""

import sys, os, timeit
defnum, defrep = 1000, 5 # May vary per stmt

def runner(stmts, pythons=None, tracemd=False):
    """
    메인 로직: 입력된 리스트에 띠라 테스트를 실행하며, 호출자는 사용 모드를 제어할 수 있다.
    stmts: [(실행 횟수?, 반복 횟수?, 문 문자열)]. stmt 안의 $slitif3을 대체
    pythons: None=현재 파이썬, 또는 [(ispy3?, 파이썬 실행 파일 경로)]
    """
    print(sys.version)
    for (number, repeat, stmt) in stmts:
        number = number or defnum
        repeat = repeat or defrep          # 0 = default

        if not pythons:
            # 현재 파이썬으로 stmt 실행: API 호출
            # 여기서는 라인을 분할하거나 인용할 필요가 없음
            ispy3 = sys.version[0] == '3'
            stmt  = stmt.replace('$listif3', 'list' if ispy3 else '')
            best  = min(timeit.repeat(stmt=stmt, number=number, repeat=repeat))
            print('%.4f [%r]' % (best, stmt[:70]))

        else:
            # 모든 파이썬에서 stmt 실행: 명령 라인
            # 인용된 인수들로 라인 분할
            print('-' * 80)
            print('[%r]' % stmt)
            for (ispy3, python) in pythons:
                stmt1 = stmt.replace('$listif3', 'list' if ispy3 else '')
                stmt1 = stmt1.replace('\t', ' ' * 4)
                lines = stmt1.split('\n')
                args = ' '.join('"%s"' % line for line in lines)
                cmd = '%s -m timeit -n %s -r %s %s' % (python, number, repeat, args)
                print(python)
                if tracemd: print(cmd)
                print('\t' + os.popen(cmd).read().rstrip())
