# 네임스페이스 중첩

X = 3


X = 2
import mod3

print(X, end=' ')               # 나의 전역 X
print(mod3.X)                   # mod3의 X


X = 1
import mod2

print(X, end=' ')               # 나의 전역 X
print(mod2.X, end=' ')          # mod2의 X
print(mod2.mod3.X)              # 중첩된 mod3의 X


# python mod1.py
# 2 3
# 1 2 3
