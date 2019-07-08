# 반환(return)이 없는 함수

def proc(x):
    print(x)                    # return이 없으면 None이 반환됨

x = proc('testing 123...')
# testing 123...
print(x)
# None


list = [1, 2, 3]
list = list.append(4)           # append는 프로시저
print(list)                     # append는 리스트를 직접 변경함
# None
