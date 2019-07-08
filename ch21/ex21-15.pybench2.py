# pybench2.py

...
def runner(stmts, pythons=None, tracemd=False):
    for (number, repeat, setup, stmt) in stmts:
        if not pythons:
            ...
            best = min(timeit.repeat(
                setup=setup, stmt=stmt, number=number, repeat=repeat))
        else:
            setup = setup.replace('\t', ' ' * 4)
            setup = ' '.join('-s "%s"' % line for line in setup.split('\n'))
            ...
            for (ispy3, python) in pythons:
                ...
                cmd = '%s -m timeit -n %s -r %s %s %s' %
                              (python, number, repeat, setup, args)


# pybench2_cases.py
import pybench2, sys
...
stmts = [                       # (num,rep,setup,stmt)
    (0, 0, "", "[x ** 2 for x in range(1000)]"),
    (0, 0, "", "res=[]\nfor x in range(1000): res.append(x ** 2)")

    (0, 0, "def f(x):\n\treturn x",
           "[f(x) for x in 'spam' * 2500]"),
    (0, 0, "def f(x):\n\treturn x",
           "res=[]\nfor x in 'spam' * 2500:\n\tres.append(f(x))"),

    (0, 0, "L = [1, 2, 3, 4, 5]", "for i in range(len(L)): L[i] += 1"),
    (0, 0, "L = [1, 2, 3, 4, 5]", "i=0\nwhile i < len(L):\n\tL[i] += 1\n\ti += 1")]
...
pybench2.runner(stmts, pythons, tracemd)
