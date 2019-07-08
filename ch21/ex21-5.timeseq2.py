# 함수 호출의 영향: map

# timeseq2.py 파일(일부 변경)
...
def forLoop():
    res = []
    for x in repslist:
        res.append(x + 10)
    return res

def listComp():
    return [x + 10 for x in repslist]

def mapCall():
    return list(map((lambda x: x + 10), repslist)) # 3.X에서만 list()

def genExpr():
    return list(x + 10 for x in repslist) # 2.X + 3.X 모두 list()

def genFunc():
    def gen():
        for x in repslist:
            yield x + 10
    return list(gen())          # 2.X + 3.X 모두 list()

print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (bestof, (total, result)) = timer.bestoftotal(5, 1000, test)
    print('%-9s: %.5f => [%s...%s]' %
          (test.__name__, bestof, result[0], result[-1]))


# c:\python36\python timeseqs2.py
3.6.0 (v3.6.0:41df79263all, Dec 23 2016, 08:06:12) [MSC v.1900 64bit (AMD64)]
forLoop  : 1.35136 => [0...9999]
listComp : 0.73730 => [0...9999]
mapCall  : 1.68588 => [0...9999]
genExpr  : 1.10963 => [0...9999]
genFunc  : 1.11074 => [0...9999]


def F(x): return x
def listComp():
    return [F(x) for x in repslist]
def mapCall():
    return list(map(F, repslist))
