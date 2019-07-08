# 타이밍 스크립트

# timeseqs.py 파일
"다양한 반복 도구들의 상대적인 속도 테스트"

import sys, timer               # timer 함수들 임포트
reps = 10000
repslist = list(range(reps))    # 2.X/3.X 모두에서 동작하도록 list로 생성

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs, repslist)) # 3.X에서만 여기서 list()를 사용!
  # return map(abs, repslist)

def genExpr():
    return list(abs(x) for x in repslist) # 결과를 강제로 생성하기 위해 list() 사용

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())          # 결과를 강제로 생성하기 위해 list() 사용

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))
