acc = input('저금액 입력\n')
acc = float(acc)
accp = input('이자율 입력(%)\n')
accp = float(accp) / 100 + 1
tax = input('과세 or 비과세\n')

if tax == '과세':
    accp = accp * 0.75
    total = acc * accp
    print(f'총 원리금은 {total}입니다.')
else:
    total = accp * acc
    print(f'총 원리금은 {total}입니다.')



# 저축액 = 5000000
# 이자 = 저축액 *0.15
# 세금 = 이자 *0.15
# 원리금 = 저축액 + 이자 - 세금

# print(f"저축액 : {저축액}원")
# print(f'이  자 : {이자}원')
# print(f'세  금 : {세금}원')
# print(f'원리금 : {원리금}원')