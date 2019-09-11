# 트리 리스터 실행하기

# py -2
# <Instance of Sub, address 140554999548240:
#  _ListTree__visited={}
#  data1=spam
#  data2=eggs
#  data3=42

# ....<Class Sub, address 140554999499072:
#      __doc__
#      __init__
#      __module__
#      spam=<unbound method Sub.spam>

# ........<Class Super, address 140554999498968:
#          __doc__
#          __init__
#          __module__
#          ham=<unbound method Super.ham>
# ........>

# ........<Class ListTree, address 140554999498552:
#          _ListTree__attrnames=<unbound method ListTree.__attrnames>
#          _ListTree__listclass=<unbound method ListTree.__listclass>
#          __doc__
#          __module__
#          __str__
# ........>
# ....>
# >


# py -3
# <Instance of Sub, address 140129096559752:
#  _ListTree__visited={}
#  data1=spam
#  data2=eggs
#  data3=42

# ....<Class Sub, address 12538792:
#      __doc__
#      __init__
#      __module__
#      spam=<function tester.<locals>.Sub.spam at 0x7f7259058c80>

# ........<Class Super, address 12537848:
#          __dict__
#          __doc__
#          __init__
#          __module__
#          __weakref__
#          ham=<function tester.<locals>.Super.ham at 0x7f7259058b70>

# ............<Class object, address 10413600:
#              __class__
#              __delattr__
#              __dir__
#              __doc__
#              __eq__
#              __format__
#              __ge__
#              __getattribute__
#              __gt__
#              __hash__
#              __init__
#              __init_subclass__
#              __le__
#              __lt__
#              __ne__
#              __new__
#              __reduce__
#              __reduce_ex__
#              __repr__
#              __setattr__
#              __sizeof__
#              __str__
#              __subclasshook__
# ............>
# ........>

# ........<Class ListTree, address 12555336:
#          _ListTree__attrnames=<function ListTree.__attrnames at 0x7f7259058620>
#          _ListTree__listclass=<function ListTree.__listclass at 0x7f72590588c8>
#          __dict__
#          __doc__
#          __module__
#          __str__
#          __weakref__

# ............<Class object:, address 10413600: (see above)>
# ........>
# ....>
# >


class C: pass
class B(C): pass
C.__bases__ = (B,)                      # 심연의 흑마술!
# TypeError: a __bases__ item causes an inheritance cycle
