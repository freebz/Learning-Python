# 사용법 변형: 더블 언더스코어가 붙은 이름 값 보여 주기

    for attr in sorted(obj.__dict__):
#       if attr.startswith('__') and attr.endswith('__'):
#           result += spaces + '{0}\n'.format(attr)
#       else:
            result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))


# py -2 listtree.py
# <Instance of Sub, address 140380095949136:
#  _ListTree__visited={}
#  data1=spam
#  data2=eggs
#  data3=42

# ....<Class Sub, address 140380095899864:
#      __doc__=None
#      __init__=<unbound method Sub.__init__>
#      __module__=testmixin
#      spam=<unbound method Sub.spam>

# ........<Class Super, address 140380095899760:
#          __doc__=None
#          __init__=<unbound method Super.__init__>
#          __module__=testmixin
#          ham=<unbound method Super.ham>
# ........>

# ........<Class ListTree, address 140380095899344:
#          _ListTree__attrnames=<unbound method ListTree.__attrnames>
#          _ListTree__listclass=<unbound method ListTree.__listclass>
#          __doc__=
#     전체 클래스 트리와 self와 그 위로 존재하는 모든 객체들의 속성에 대한 __str__ 추적 결과를 반환하는 혼합 클래스
#     | print()로 실행되며, str()은 구성된 문자열을 반환
#     클라이언트에 영향을 주는 것을 피하기 위해 __X 속성 이름 사용
#     명시적으로 슈퍼클래스로 재귀함, 명확성을 위해 str.format()을 사용
    
#          __module__=__main__
#          __str__=<unbound method ListTree.__str__>
# ........>
# ....>
# >


# py -3 listtree.py
#    ...등등...
#    File "listtree.py", line 18, in __attrnames
#     result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
# TypeError: type method_descriptior doesn't define __format__


# py -3.1
'{0}'.format(object.__reduce__)
# "<method '__reduce__' of 'object' objects>"
# py -3.3
'{0}'.format(object.__reduce__)
# TypeError: Type method_descriptor doesn't define __format__


# py -3.3
'{0:s}'.format(object.__reduce__)
# TypeError: Type method_descriptor doesn't define __format__
'{0!s}'.format(object.__reduce__)
# "<method '__reduce__' of 'object' objects>"
'{0}'.format(str(object.__reduce__))
# "<method '__reduce__' of 'object' objects>"


# py -3.3
'%s' % object.__reduce__
# "<method '__reduce__' of 'object' objects>"


result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
result += spaces + '%s=%s\n' % (attr, getattr(obj, attr))
