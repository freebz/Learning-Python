# 객체 지향 프로그래밍과 코드 재사용

# 다형성과 클래스

class Employee:                     # 공통 슈퍼클래스
    def computeSalary(self): ...    # 공통 혹은 기본 동작
    def giveRaise(self): ...
    def promote(self): ...
    def retire(self): ...


class Engineer(Employee):           # 특수화된 서브클래스
    def computeSalary(self): ...    # 그 외의 커스터마이즈된 동작은 여기 위치함


bob = Employee()                # 기본 메서드
sue = Employee()                # 기본 메서드
tom = Engineer()                # 엔지니어에 맞게 커스터마이즈된 급여 산정 메서드


company = [bob, sue, tom]       # 복합 객체
for emp in company:
    print(emp.computeSalary())  # 객체에 따라 기본 버전 또는 커스터마이즈된 버전이 실행됨


def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if not data:break
        data = converter(data)
        writer.write(data)


class Reader:
    def read(self): ...         # 기본 동작과 도구
    def other(self): ...
class FileReader(Reader):
    def read(self): ...         # 지역 파일에서 데이터를 읽음
class SocketReader(Reader):
    def read(self): ...         # 네트워크 소켓에서 데이터를 읽음
...
processor(FileReader(...),   Converter, FileWriter(...))
processor(SocketReader(...), Converter, TapeWriter(...))
processor(FtpReader(...),    Converter, XmlWriter(...))
