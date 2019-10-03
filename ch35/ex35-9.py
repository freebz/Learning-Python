# 예외 메서드 제공하기

from __future__ import print_function    # 2.X 호환

class FormatError(Exception):
    logfile = 'formaterror.txt'
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logerror(self):
        log = open(self.logfile, 'a')
        print('Error at:' , self.file, self.line, file=log)

def parser():
    raise FormatError(40, 'spam.txt')

if __name__ == '__main__':
    try:
        parser()
    except FormatError as exc:
        exc.logerror()


# del formaterror.txt
# py -3 excparse.py
# py -2 excparse.py
# type formaterror.txt
# Error at: spam.txt 40
# Error at: spam.txt 40


class CustomFormatError(FormatError):
    def logerror(self):
        ...여기만의 유일한 그 무엇...

raise CustomFormatError(...)
