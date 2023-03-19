# 슬라이싱 응용
'''
a[start, end, step]
start : 슬라이싱 시작위치
end : 슬라이싱 끝낼 위치 end-1
step : 몇개씩 끊어서 가지고 올건지

'''
a = ['a','b','c','d','e']
print(a[ : -1])
print(a[-3 : ])

print(a[ : : 2])
print(a[-5 : : 3])

print(a[ :  : -1])
print(a[3 : : -1])
print(a[1 : -1 : 2])
# step이 양수 : 오른쪽으로 움직이는 것
# step이 음수 : 왼쪽으로 움직이는 것 (거꾸로)
