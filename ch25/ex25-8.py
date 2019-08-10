# 모듈 검색 경로 변경

import sys
sys.path
# ['', '/usr/lib/python36.zip', '/usr/lib/python3.6', '/usr/lib/python3.6/lib-dynload', '/home/fx/.local/lib/python3.6/site-packages', '/usr/local/lib/python3.6/dist-packages', '/usr/lib/python3/dist-packages']

sys.path.append('C:\\sourcedir') # 모듈 검색 경로 확장
import string                    # 모든 임포트는 마지막의 새로운 디렉터리를 검색


sys.path = [r'd:\temp']         # 모듈 검색 경로 변경
sys.path.append('c:\\lp5e\\examples') # 이 샐행(프로세스)에 대해서만
sys.path.insert(0, '..')
sys.path
# ['..', 'd:\\temp', 'c:\\lp5e\\examples']
import string
# ImportError: No module named 'string'
