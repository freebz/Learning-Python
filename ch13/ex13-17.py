# 루프 코딩 기법/기술

# 루프 카운터: range

list(range(5)), list(range(2, 5)), list(range(0, 10, 2))
# ([0, 1, 2, 3, 4], [2, 3, 4], [0, 2, 4, 6, 8])


list(range(-5, 5))
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

list(range(5, -5, -1))
# [5, 4, 3, 2, 1, 0, -1, -2, -3, -4]


for i in range(3):
    print(i, 'Pythons')

# 0 Pythons
# 1 Pythons
# 2 Pythons
