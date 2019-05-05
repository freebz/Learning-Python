# PyDoc: help 함수

import sys
help(sys.getrefcount)
# Help on built-in function getrefcount in module sys:

# getrefcount(...)
#     getrefcount(object) -> integer
    
#     Return the reference count of object.  The count returned is generally
#     one higher than you might expect, because it includes the (temporary)
#     reference as an argument to getrefcount().


help(sys)
# Help on built-in module sys:

# NAME
#     sys

# MODULE REFERENCE
#     https://docs.python.org/3.6/library/sys
#     ...생략...

# DESCRIPTION
#     This module provides access to some objects used or maintained by the
#     interpreter and to functions that interact strongly with the interpreter.
#     ...생략...

# FUNCTIONS
#     __displayhook__ = displayhook(...)
#         displayhook(object) -> None
#     ...생략...

# DATA
#     __stderr__ = <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF...
#     __stdin__ = <_io.TextIOWrapper name='<stdin>' mode='r' encoding='UTF-8...
#     __stdout__ = <_io.TextIOWrapper name='<stdout>' mode='w' encoding='UTF...
#     ...생략...

# FILE
#     (built-in)


help(dict)
# Help on class dict in module builtins:

# class dict(object)
#  |  dict() -> new empty dictionary
#  |  dict(mapping) -> new dictionary initialized from a mapping object's
#  ...생략...

help(str.replace)
# Help on method_descriptor:

# replace(...)
#     S.replace(old, new[, count]) -> str
    
#     Return a copy of S with all occurrences of substring
#     ...생략...

help(''.replace)
# ...이전 결과와 유사...

help(ord)
# Help on built-in function ord in module builtins:

# ord(c, /)
#     Return the Unicode code point for a one-character string.


import docstrings
help(docstrings.square)
# Help on function square in module docstrings:

# square(x)
#     function documentation
#     can we have your liver then?

help(docstrings.Employee)
# Help on class Employee in module docstrings:

# class Employee(builtins.object)
#  |  class documentation
#  |  
#  ...생략...

help(docstrings)
# Help on module docstrings:

# NAME
#     docstrings

# DESCRIPTION
#     Module documentation
#     Words Go Here

# CLASSES
#     builtins.object
#         Employee
    
#     class Employee(builtins.object)
#      |  class documentation
#      |  
#      ...생략...

# FUNCTIONS
#     square(x)
#         function documentation
#         can we have your liver then?

# DATA
#     spam = 40

# FILE
#     /code/docstrings.py
