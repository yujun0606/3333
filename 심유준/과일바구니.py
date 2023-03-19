#과일바구니
fruit = ['사과', '바나나', '딸기', '키위', '귤', '사과']

print(len(fruit))

apple = fruit.count('사과')

print(apple)

del fruit[-1]
print(fruit)

fruit.insert(2, '복숭아')
print(fruit)
#리스트 안에 있는지 없는지 확인 할때 사용 
if '사과' in fruit:
    print('사과가 바구니에 있습니다.')
if '바나나' not in fruit:
    print('바나나 구입하자.')

# for문
for i in range(3):
    print('안녕')
for i in range(0, 3, 1):
    print('안녕')
#for문 + list
    list_food = ['햄버거', '치킨', '피자']
for food in list_food:
    print(food)

for i in [1, 2, 3, 4, 5]:
    print(i)
    print("hello")
hi = "안녕하세요"
for s in hi:
    print(s)
