전화번호 = input('휴대전화 번호 입력 :')
앞번호 = 전화번호.split('-')[0]
if 앞번호 == "011":
    print("당신은 skt 사용자 입니다.")
elif 앞번호 == "016":
    print("당신은 kt 사용자 입니다.")
elif 앞번호 == "019":
    print("당신은 lgu 사용자 입니다.")
else:
    print("알수없음")
    
