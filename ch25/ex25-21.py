# reload, from, 대화형 테스트

from module import function
function(1, 2, 3)


from imp import reload
reload(module)


from imp import reload
import module
reload(module)
function(1, 2, 3)


from imp import reload
import module
reload(module)
from module import function     # 또는 포기하고 module.function() 사용
function(1, 2, 3)
