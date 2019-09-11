# 콜렉터 모듈

# lister.py 파일
# 편의를 위해 세 개의 lister를 한 모듈에 모아둠

from listinstance  import ListInstance
from listinherited import ListInherited
from listtree      import ListTree

Lister = ListTree                           # 기본 lister 선택


import lister
lister.ListInstance                         # 특정 lister 사용
# <class 'listinstance.ListInstance'>
lister.Lister                               # 기본값 Lister 사용
# <class 'listtree.ListTree'>

from lister import Lister                   # 기본값 Lister 사용
Lister
# <class 'listtree.ListTree'>

from lister import ListInstance as Lister   # Lister 별칭 사용
Lister
# <class 'listinstance.ListInstance'>
