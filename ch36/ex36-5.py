# 함수는 raise를 이용하여 상태를 알릴 수 있음

class Found(Exception): pass

def searcher():
    if ...성공...:
        raise Found()           # 플레그를 반환하는 대신 예외를 발생시킴
    else:
        return
try:
    searcher()
except Found:                   # 아이템이 발견될 경우, 예외
    ...성공...
else:                           # 발견 못하면 반환: not found
    ...실패...


class Failure(Exception): pass

def searcher():
    if ...성공...:
        return ...검색 결과...
    else:
        raise Failure()

try:
    item = searcher()
except Failure:
    ...검색 결과 없음...
else:
    ...검색 결과 활용...
