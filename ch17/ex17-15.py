# 3.X에서의 nonlocal문

# nonlocal의 기본

def func():
    nonlocal name1, name2, ...  # 여기서는 OK!

nonlocal X
# SyntaxError: nonlocal declaration not allowed at module level
