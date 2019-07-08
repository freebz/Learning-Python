# timeit을 이용한 반복과 파이썬 성능 측정

# 기본적인 timeit 사용법

# 대화형 사용법과 API 호출

# py -3
import timeit
min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5))
# 0.5062382371756811

# py -2
import timeit
min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5))
# 0.0708020004193198

# c:\pypy\pypy-1.9\pypy.exe
import timeit
min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]", number=1000, repeat=5))
# 0.0059330329674303905
