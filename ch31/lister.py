# -*- coding: utf-8 -*-
# lister.py 파일
# 편의를 위해 세 개의 lister를 한 모듈에 모아둠

from listinstance  import ListInstance
from listinherited import ListInherited
from listtree      import ListTree

Lister = ListTree                           # 기본 lister 선택
