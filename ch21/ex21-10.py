# 여러 라인의 문(statement) 측정하기

# py -3
import timeit
min(timeit.repeat(number=10000, repeat=3,
    stmt="L = [1, 2, 3, 4, 5]\nfor i in range(len(L)): L[i] += 1"))
# 0.01397292797131814

min(timeit.repeat(number=10000, repeat=3,
    stmt="L = [1, 2, 3, 4, 5]\ni=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1"))
# 0.015452276471516813

min(timeit.repeat(number=10000, repeat=3,
    stmt="L = [1, 2, 3, 4, 5]\nM = [x + 1 for x in L]"))
# 0.009464995838568635


py -3 -m timeit -n 1000 -r 3 "L = [1,2,3,4,5]" "i=0" "while i < len(L):"
 "    L[i] += 1" "    i += 1"
1000 loops, best of 3: 1.54 usec per loop

py -3 -m timeit -n 1000 -r 3 "L = [1,2,3,4,5]" "M = [x + 1 for x in L]"
1000 loops, best of 3: 0.959 usec per loop
