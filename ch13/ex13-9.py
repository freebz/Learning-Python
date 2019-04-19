# 더 생각해 볼 주제: C while 루프 흉내 내기

while ((x = next(obj)) != NULL) {...x 처리 작업...}


while True:
    x = next(boj)
    if not x: break
    ...x 처리 작업...


x = True
while x:
    x = next(obj)
    if x:
        ...x 처리 작업...


x = next(obj)
while x:
    ...x 처리 작업...
    x = next(obj)


for x in obj: ...x 처리 작업...
