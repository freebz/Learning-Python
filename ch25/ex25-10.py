# 예제: 모듈은 객체

M.name                          # 객체에 의해 속성 인정
M.__dict__['name']              # 직접 네임스페이스 딕셔너리를 인덱싱
sys.modules['M'].name           # 직접 적재된 모듈을 갖는 테이블을 인덱싱
getattr(M, 'name')              # 속성을 가져오는 내장된 함수 호출


import mydir
import tkinter
mydir.listing(tkinter)
------------------------------------------------------------
name: tkinter file: /usr/lib/python3.6/tkinter/__init__.py
------------------------------------------------------------
00) ACTIVE active
01) ALL all
02) ANCHOR anchor
03) ARC arc
04) BASELINE baseline
...생략...
156) mainloop <function mainloop at 0x7f3341ca22f0>
157) re <module 're' from '/usr/lib/python3.6/re.py'>
158) sys <module 'sys' (built-in)>
159) wantobjects 1
------------------------------------------------------------
tkinter has 160 names
------------------------------------------------------------
