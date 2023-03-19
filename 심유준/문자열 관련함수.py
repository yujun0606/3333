# 문자열 관련 함수
# join, split, upper, lower, replace, lstrip, rstrip, strip

# 문자열 삽입(join)
print(":".join('abcd'))
print("-".join('01055556666'))

#문자열 나누기(split)
a = 'a:b:c:d'
print(a.split(':'))

b = 'a b c d'
print(b.split())

#문자열 바꾸기(replace)
c = 'I like a dog'
print(c.replace('dog','cat'))
a = "a,b,c,d,e"
print(a.replace(',', '/'))
print(a.replace(',', '/', 1))
print(a.replace(',', '/', 2))

# 소문자를 대문자로 바꾸기(upper)
a = 'cat'
print(a.upper())

# 대문자를 소문자로  바꾸기(lower)
a = 'CAT'
print(a.lower())

#왼쪽 공백 지우기(lstrip)
a = ' hi '
print(a.lstrip())
#오른쪽 공백 지우기(rstrip)
a = ' hi '
print(a.rstrip())
a = ' hi '
print(a.strip())

#맨 첫글자만 대문자로 변환(capitalize)
a =  'cat'
print(a.capitalize())



















