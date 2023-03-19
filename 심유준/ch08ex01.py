cart = []
cart.append('사과')
cart.append('수박')
print(cart)
pack = []
pack.append('홈런볼')
pack.append('우유')
print(pack)

a = cart + pack

print(a)

cart = ['사과', '수박', '홈런볼', '우유']
b = []
for i in cart:
    a = i.replace('수박', '멜론')
    b.append(a)
print(b)

'''del cart[3]
pack.append('요거트')
cart.remove('요거트')'''

print()


