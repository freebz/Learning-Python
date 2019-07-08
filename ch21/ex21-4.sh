# 타이밍 결과

# c:\python36\python timeseqs.py
3.6.0 (v3.6.0:41df79263all, Dec 23 2016, 08:06:12) [MSC v.1900 64bit (AMD64)]
forLoop  : 1.33290 => [0...9999]
listComp : 0.69658 => [0...9999]
mapCall  : 0.56483 => [0...9999]
genExpr  : 1.08457 => [0...9999]
genFunc  : 1.07623 => [0...9999]


return [abs(x) for x in repslist]        # 0.69초
return list(abs(x) for x in repslist)    # 1.08초: 내부적으로 다름


# c:\python27\python timeseqs.py
2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)]
forLoop  : 1.24902 => [0...9999]
listComp : 0.66970 => [0...9999]
mapCall  : 0.57018 => [0...9999]
genExpr  : 0.90339 => [0...9999]
genFunc  : 0.90542 => [0...9999]


# c:\PyPy\pypy-1.9\pypy.exe timeseqs.py
2.7.2 (341e1e3821ff, Jun 07 2012, 15:43:00)
[PyPy 1.9.0 with MSC v.1500 32 bit]
forLoop  : 0.10106 => [0...9999]
listComp : 0.05629 => [0...9999]
mapCall  : 0.10022 => [0...9999]
genExpr  : 0.17234 => [0...9999]
genFunc  : 0.17519 => [0...9999]
