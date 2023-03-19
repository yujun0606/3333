itzy = ['예지', '류진', '리아', '유나', '채령']

# 리스트 수정하기
itzy[0] = '조이'
print(itzy)

#슬라이싱을 통해서 여러값 한번에 바꾸기
itzy[0 : 3] = '아이린' , '웬디', '슬기'
print(itzy)

# append() 맨뒤에 추가 
itzy.append('아이유')
print(itzy)

#insert()
itzy.insert(1, '카리나')
print(itzy)
itzy.insert(3, "윈터")
print(itzy)

# remove()
itzy.remove('아이유')
print(itzy)
# del
del itzy[1]
print(itzy)

#len
print(len(itzy))
