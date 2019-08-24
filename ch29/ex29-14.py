# 문서화 문자열 다시 살펴보기

"I am: docstr.__doc__"

def func(args):
    "I am: docstr.func.__doc__"
    pass

class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)


import docstr
docstr.__doc__
# 'I am: docstr.__doc__'
docstr.func.__doc__
# 'I am: docstr.func.__doc__'
docstr.spam.__doc__
# 'I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__'
docstr.spam.method.__doc__
# 'I am: spam.method.__doc__ or self.method.__doc__'

x = docstr.spam()
x.method()
# I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__
# I am: spam.method.__doc__ or self.method.__doc__


help(docstr)
# Help on module docstr:

# NAME
#     docstr - I am: docstr.__doc__

# CLASSES
#     builtins.object
#         spam
    
#     class spam(builtins.object)
#      |  I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__
#      |  
#      |  Methods defined here:
#      |  
#      |  method(self)
#      |      I am: spam.method.__doc__ or self.method.__doc__
#      |  
#      |  ----------------------------------------------------------------------
#      |  Data descriptors defined here:
#      |  
#      |  __dict__
#      |      dictionary for instance variables (if defined)
#      |  
#      |  __weakref__
#      |      list of weak references to the object (if defined)

# FUNCTIONS
#     func(args)
#         I am: docstr.func.__doc__

# FILE
#     /home/fx/work/Learning Python/ch29/docstr.py
