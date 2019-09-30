# 파이썬 3.X 예외 체인: raise from

raise newexception from otherexception


try:
    1 / 0
except Exception as E:
    raise TypeError('Bad') from E # 명시적인 예외 체인

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# ZeroDivisionError: division by zero

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# TypeError: Bad


try:
    1 / 0
except:
    badname                     # 묵시적인 예외 처리

# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# ZeroDivisionError: division by zero

# During handling of the above exception, another exception occurred:

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
# NameError: name 'badname' is not defined


try:
    try:
        raise IndexError()
    except Exception as E:
        raise TypeError() from E
except Exception as E:
    raise SyntaxError() from E

# Traceback (most recent call last):
#   File "<stdin>", line 3, in <module>
# IndexError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<stdin>", line 5, in <module>
# TypeError

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "<stdin>", line 7, in <module>
# SyntaxError: None


try:
    try:
        1 / 0
    except:
        badname
except:
    open('nonesuch')
