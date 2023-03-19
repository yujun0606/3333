num = input("휴대전화 번호 입력 :")
phone = num.split('-')[0]


if phone == '011':
    1 = "SKT"
elif phone == '016':
    1 = "KT"
elif phone == '019':
    1 = "LGU"
else:
    1 = "알수없음"

print(f"당신은 {1}사용자입니다")
