# 일반 연산자 오버로딩 메서드

# py -3 -m timeit -n 1000 -r 5
#          -s "L = list(range(100))" "x = L.__len__()"
# 1000 loops, best of 5:0.134 usec per loop

# py -3 -m timeit -n 1000 -r 5
#          -s "L = list(range(100))" "x = len(L)"
# 1000 loops, best of 5: 0.063 usec per loop

# py -2 -m timeit -n 1000 -r 5
#          -s "L = list(range(100))" "x = L.__len__()"
# 1000 loops, best of 5: 0.117 usec per loop

# py -2 -m timeit -n 1000 -r 5
#          -s "L = list(range(100))" "x = len(L)"
# 1000 loops, best of 5: 0.0596 usec per loop
