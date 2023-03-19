bs = ['파이썬', 'c', '캐드', '포토샵','JAVA','엑셀']

bs.append('파워포인트')
bs.remove('JAVA')
bs.insert(3, "일러스트")
print(bs)
print(len(bs))
b = input("도서 이름 : ")
if b in bs:
    print("대여가능")
