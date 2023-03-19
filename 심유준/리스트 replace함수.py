#리스트 + replace함수

food = ['떡볶이', '곱창', '삼겹살', '초밥']
b = [] #빈리스트 만든다.
for i in food:
    a = i.replace('삼겹살', '소고기')
    b.append(a)
print(b)
