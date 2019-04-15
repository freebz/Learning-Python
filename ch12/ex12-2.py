# 다중 분기

x = 'killer rabbit'
if x == 'roger':
    print("shave and a haircut")
elif x == 'bugs':
    print("what's up doc?")
else:
    print('Run away! Run away!')

# Run away! Run away!


choice = 'ham'
print({'spam': 1.25,            # 딕셔너리 기반의 'switch'
       'ham': 1.99,             # 기본값이 필요한 경우 has_key 또는 get을 이용
       'eggs': 0.99,
       'bacon': 1.10}[choice])
# 1.99


if choice == 'spam':            # if문으로 작성한 같은 기능
    print(1.25)
elif choice == 'ham':
    print(1.99)
elif choice == 'eggs':
    print(0.99)
elif choice == 'bacon':
    print(1.10)
else:
    print('Bad choice')

# 1.99
