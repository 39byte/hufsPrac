print('=== 원리금 계산 프로그램 ===')

Bal = 5_000_000; PlsMn = Bal * 0.0375; Tax = PlsMn * 0.15
Total = Bal + PlsMn - Tax

print(f"원  금 : {Bal:10,.0f}원")
print(f"이  자 : {PlsMn:10,.0f}원")
print(f"세  금 : {Tax:10,.0f}원")
print(f"원리금 : {Total:10,.0f}원")