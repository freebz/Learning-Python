# 더 생각해 볼 주제: print와 stdout

class FileFaker:
    def write(self, string):
        # string에 담긴 출력된 텍스트로 작업을 수행

import sys
sys.stdout = FileFaker()
print(someObjects)              # 클래스 write 메서드로 보내기


myobj = FileFaker()             # 3.X: 한 번의 인쇄를 위해 객체로 리다이렉트
print(someObjects, file=myobj)  # sys.stdout을 재설정하지 않음

myobj = FileFaker()             # 2.X: 동일한 효과
print >> myobj, someObjects     # sys.stdout을 재설정하지 않음


python script.py < inputfile > outputfile
python script.py | filterProgram
