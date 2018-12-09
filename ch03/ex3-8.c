#include <Python.h>
...
Py_Initialize();		                   // 파이썬이 아닌 C 코드
PyRun_SimpleString("x = 'brave ' + 'sir robin'");  // ㄱ러나 파이썬 코드를 실행하 ㄹ수 있음
