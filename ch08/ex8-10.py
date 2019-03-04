# 딕셔너리 변경하기

D
# {'spam': 2, 'ham': 1, 'eggs': 3}

D['ham'] = ['grill', 'bake', 'fry']
D
# {'spam': 2, 'ham': ['grill', 'bake', 'fry'], 'eggs': 3}

del D['eggs']                   # 항목 삭제
D
# {'spam': 2, 'ham': ['grill', 'bake', 'fry']}

D['brunch'] = 'Bacon'           # 새 항목 추가
D
# {'spam': 2, 'ham': ['grill', 'bake', 'fry'], 'brunch': 'Bacon'}
