# 콘텍스트 관리 프로토콜

class TraceBlock:
    def message(self, arg):
        print('running ' + arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            return False                      # 전파

if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test 1')
        print('reached')

    with TraceBlock() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')


# py -3 withas.py 
# starting with block
# running test 1
# reached
# exited normally

# starting with block
# running test 2
# raise an exception! <class 'TypeError'>
# Traceback (most recent call last):
#   File "withas.py", line 22, in <module>
#     raise TypeError
# TypeError
