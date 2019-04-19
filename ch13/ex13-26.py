# 더 생가ㅐ ㅎ게줒 롭: 셸 명령과 그 외

import os
F = os.popen('dir')             # 라인 단위로 읽기
F.readline()
# ' Volumn in drive c has no label.\n'
F = os.popen('dir')             # 고정된 크기의 블록 읽기
F.read(50)
# ' Volumn in drive C has no label.\n Volume Serial Nu'

os.popen('dir').readlines()[0]  # 전체 라인 읽기: 인덱스
# ' Volumn in drive C has no label.\n'
os.popen('dir').read()[:50]     # 한 번에 모두 읽기: 슬라이스
# ' Volumn in drive C has no label.\n Volume Serial Nu'

for line in os.popen('dir'):    # 파일 라인 반복자 루프
    print(line.rstrip())

#  Volumn in drive C has no label.
#  Volume Serial Number is D093-D1F7
# ...등등...


os.system('systeminfo')
# ...콘솔에서 출력, IDLE에서 팝업...
# 0
for line in os.popen('systeminfo'): print(line.rstrip())

# Host Name:             MARK-VAIO
# OS Name:               Microsoft Windows 7 Professional
# OS Version:            6.1.7601 Service Pack 1 Build 7601
# ...다양한 시스템 정보 텍스트...


# 서식 지정 및 제한된 출력
for (i, line) in enumerate(os.popen('systeminfo')):
    if i == 4: break
    print('%05d) %s' % (i, line.rstrip()))

# 00000)
# 00001) Host Name:             MARK-VAIO
# 00002) OS Name:               Microsoft Windows 7 Professional
# 00003) OS Version:            6.1.7601 Service Pack 1 Build 7601


# 대소문자에 상관없이 특정 라인 분석
for line in os.popen('systeminfo'):
    parts = line.split(':')
    if parts and parts[0].lower() == 'system type':
        print(parts[1].strip())

# x64-based PC


# awk 따라 하기: 공백으로 구분된 파일로부터 일곱 개의 열 추출
for val in [line.split()[6] for line in open('input.txt')]:
    print(val)

# 동일하지만 결과를 보관하고 있는 좀 더 명확한 코드
col7 = []
for line in open('input.txt'):
    cols = line.split()
    col7.append(cols[6])
for item in col7: print(item)

# 동일하지만 재사용 가능한 함수(이 책의 다음 파트에서 다룬다)
def awker(file, col):
    return [line.rstrip().split()[col-1] for line in open(file)]

print(awker('input.txt', 7))              # 문자열들의 리스트
print(','.join(awker('input.txt', 7)))    # 사이에 콤마 출력


from urllib.request import urlopen
for line in urlopen('http://learing-python.com/books'):
    print(line)

# b'<HTML>\n'
# b'\n'
# b'<HEAD>\n'
# b"<TITLE>Mark Lutz's Book Support Site</TITLE>\n"
# ...등...
