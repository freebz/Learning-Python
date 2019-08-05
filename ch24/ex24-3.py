# 패키지 __init__.py 파일

dir0\dir1\dir2\mod.py


import dir1.dir2.mod


dir0\                           # 모듈 검색 경로에서 컨테이너
    dir1\
       __init__.py
       dir2\
           __init__.py
           mod.py
