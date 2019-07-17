# 모듈 네임스페이스

# 파일은 네임스페이스를 생성

print('starting to load...')
import sys
name = 42

def func(): pass
class klass: pass

print('done loading.')


import module2
# starting to load...
# done loading.


module2.sys
# <module 'sys' (built-in)>

module2.name
# 42

module2.func
# <function func at 0x7fd032741950>

module2.klass
# <class 'module2.klass'>
