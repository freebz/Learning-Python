# break

while True:
    name = input('Enter name:') # 2.X에서 raw_input() 사용
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)

# Enter name:bob
# Enter age: 40
# Hello bob => 1600
# Enter name:sue
# Enter age: 30
# Hello sue => 900
# Enter name:stop
