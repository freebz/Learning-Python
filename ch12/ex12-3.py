# 기본 상황 처리하기

branch = {'spam': 1.25,
          'ham': 1.99,
          'eggs': 0.99}

print(branch.get('spam', 'Bad choice'))
# 1.25
print(branch.get('bacon', 'Bad choice'))
# Bad choice


choice = 'bacon'
if choice in branch:
    print(branch[choice])
else:
    print('Bad choice')

# Bad choice


try:
    print(branch[choice])
except KeyError:
    print('Bad choice')

# Bad choice
