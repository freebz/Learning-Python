# 파일은 여전히 디렉터리에 우선함

# mkdir ns2
# mkdir ns3
# mkdir   ns3\dir
# notepad ns3\dir\ns2.py
# type    ns3\dir\ns2.py
print(r'ns3\dir\ns2.py')


# set PYTHONPATH=               # PYTHONPATH 비구이
# py-3.2

import ns2
# ImportError: No module named ns2

# py -3.6
import ns2
ns2                             # CWD 내 단일 디렉터리 네임스페이스 패키지
# <module 'ns2' (namespace)>
ns2.__path__
# _NamespacePath(['.\\ns2'])


# set PYTHONPATH=C:\code\ns3\dir
# py -3.6
import ns2                      # 동일 이름의 디렉터리가 아니라 나중에 발견된 파일을 사용!
# ns3\dir\ns2.py!
ns2
# <module 'ns2' from 'C:\\code\\ns3\\dir\\ns2.py'>
import sys
sys.path[:2]                    # 첫 항목인 ''는 CWD(현재 작업 중인 디렉터리)를 의미함
# ['', 'C:\\code\\ns3\\dir']


# py -3.2
import ns2
# ns3]dir\ns2.py!
ns2
# <module 'ns2' from 'C:\code\ns3\dir\ns2.py'>


# mkdir ns4\dir1\sub
# mkdir ns4\dir2\sub
# set PYTHONPATH=c:\code\ns4\dir1;c:\code\ns4\dir2
# py -3
import sub
sub
# <module 'sub' (namespace)>
sub.__path__
# _NamespacePath(['c:\\code\\ns4\\dir1\\sub', 'c:\\code\\ns4\\dir2\\sub'])


# notepad ns4\dir2\sub\__init__.py
# py -3
import sub                      # 나중에 발견된 일반 패키지 사용. 동일한 이름의 디렉터리가 아니라!
sub
# <module 'sub' from 'c:\\code\\ns4\\dir2\\sub\\__init__.py'>
