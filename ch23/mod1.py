X = 1
import mod2

print(X, end=' ')               # 나의 전역 X
print(mod2.X, end=' ')          # mod2의 X
print(mod2.mod3.X)              # 중첩된 mod3의 X
