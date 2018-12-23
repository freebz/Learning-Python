# 파일

f = open('data.txt', 'w')       # 출력 모드로 새 파일을 만듦('w'는 쓰기)
f.write('Hello\n')              # 문자들의 문자열을 파일에 씀
# 6
f.write('world\n')              # 파이썬 3.X에서 파일에 쓴 항목 수를 반환
# 6
f.close()                       # 출력 버퍼를 디스크로 flush하기 위해 종료


f = open('data.txt')            # 'r'(읽기)는 기본 처리 모드
text = f.read()                 # 파일 전체를 문자열로 읽음
text
# 'Hello\nworld\n'

print(text)                     # print는 제어 문자들을 해석
# Hello
# world
#

text.split()                    # 파일 콘텐츠는 항상 문자열임
# ['Hello', 'world']


for line in open('data.txt'): print(line)


dir(f)
# ['_CHUNK_SIZE', '__class__', '__del__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_checkClosed', '_checkReadable', '_checkSeekable', '_checkWritable', '_finalizing', 'buffer', 'close', 'closed', 'detach', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'line_buffering', 'mode', 'name', 'newlines', 'read', 'readable', 'readline', 'readlines', 'seek', 'seekable', 'tell', 'truncate', 'writable', 'write', 'writelines']
