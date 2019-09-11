# 스트림 프로세서 복습

def processor(reader, converter, writer):
    while True:
        data = reader.read()
        if not data: break
        data = converter(data)
        writer.write(data)


class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while True:
            data = self.reader.readline()
            if not data: break
            data = self.converter(data)
            self.writer.write(data)

    def converter(self, data):
        assert False, 'converter must be defined'    # 또는 예외를 발생시킴


from streams import Processor

class Uppercase(Processor):
    def converter(self, data):
        return data.upper()

if __name__ == '__main__':
    import sys
    obj = Uppercase(open('trispam.txt'), sys.stdout)
    obj.process()


# type trispam.txt
# spam
# Spam
# SPAM!

# python converters.py 
# SPAM
# SPAM
# SPAM!


# python
import converters
prog = converters.Uppercase(open('trispam.txt'), open('trispamup.txt', 'w'))
prog.process()

# type trispamup.txt
# SPAM
# SPAM
# SPAM!


# python
from converters import Uppercase

class HTMLize:
    def write(self, line):
        print('<PRE>%s</PRE>' % line.rstrip())

Uppercase(open('trispam.txt'), HTMLize()).process()
# <PRE>SPAM</PRE>
# <PRE>SPAM</PRE>
# <PRE>SPAM!</PRE>
