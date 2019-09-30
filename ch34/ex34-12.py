# 통합된 try 예제

# mergedexc.py 파일(파이썬 3.X + 2.X)
sep = '-' * 45 + '\n'


print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')


print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x = 1 / 0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


# py -3 mergedexec.py
# ---------------------------------------------
# EXCEPTION RAISED AND CAUGHT
# except run
# finally run
# after run
# ---------------------------------------------
# NO EXCEPTION RAISED
# finally run
# after run
# ---------------------------------------------
# NO EXCEPTION RAISED, WITH ELSE
# else run
# finally run
# after run
# ---------------------------------------------
# EXCEPTION RAISED BUT NOT CAUGHT
# finally run
# Traceback (most recent call last):
#   File "mergedexc.py", line 39, in <module>
#     x = 1 / 0
