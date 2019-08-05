# 세 시스템 이야기

system1\
    utilities.py                # 공통 유틸리티 함수. 클래스
    main.py                     # 프로그램 시작을 위해 이 파일을 실행
    other.py                    # 내 도구를 적재하기 위해 utilities를 임포트


system2\
    utilities.py                # 공통 유틸리티
    main.py                     # 이 파일로 실행
    other.py                    # utilities 임포트


import utilities
utilities.func('spam')


root\
    system1\
        __init__.py
        utilities.py
        main.py
        other.py
    system2\
        __init__.py
        utilities.py
        main.py
        other.py
    system3\                    # 여기 또는 다른 곳에
        __init__.py             # 다른 곳에서 임포트될 경우에만 여기에 __init__.py 필요
        myfile.py               # 여기에는 여러분의 새로운 코드가


import system1.utilities
import system2.utilities
system1.utilities.function('spam')
system2.utilities.function('eggs')
