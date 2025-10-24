func_ans = 0      #무슨 연산할지
num_ans = 0      #무슨 숫자 넣을지
num_list = []    #숫자 내역
func_list = []    #연산 내역


while func_ans != '=':       #등호 입력한 거 아니면 반복
    num_ans = 0             #초기화
    func_ans = 0
    
    #제대로 된 숫자 넣을 때까지 반복
    while True:
        #int화한 숫자 답변 저장
        try:
            num_ans = input('숫자를 입력하세요.\n')
            num_ans_int = int(num_ans)
            num_list.append(num_ans_int)
            break
        #만일 숫자 아니면 뱉기
        except ValueError:
            print('\n올바르지 않은 값입니다.')
            continue
    print('\n입력 성공')
    print(f'입력 숫자는 {num_ans_int}이고, 입력 내역은 {num_list}입니다.')

    #제대로 된 기호 넣을 때까지 반복
    while func_ans != '+' or func_ans !='-' or func_ans !='*' or func_ans !='/' or func_ans !='=':
        func_ans = input('원하는 계산을 입력하세요.(+, -, *, /, =)\n')
        if func_ans == '+' or func_ans =='-' or func_ans =='*' or func_ans =='/'or func_ans =='=':
            func_list.append(func_ans)
            print('\n입력 성공')
            print(f'입력 연산은 {func_ans}이고, 연산 내역은 {func_list}입니다.')
            break
        else:
            print('\n잘못된 기호입니다. 다시 입력해주세요.')
            continue

# mul_list = []      #곱하기 나누기 내역
# mul_index = []      #곱하기 나누기 위치들

# pls_list = []      #더하기 빼기 내역
# pls_index = []      #더하기 빼기 위치들

for i, j in enumerate(func_list):       # j : 인덱스 내뱉기, i : 연산자 내뱉기
    if j == '*':
        t = num_list[i] * num_list[i+1]
        num_list[i] = t
        del num_list[i+1]
        del func_list[i]
    elif j == '/':
        try:
            t = num_list[i] / num_list[i+1]
            num_list[i] = t
            del num_list[i+1]
            del func_list[i]
        except ZeroDivisionError:
            print('0으로 나눌 수 없습니다.\n')
            break
    elif j == '+' or j == '-':
        continue
    else:
        print('error')
        break

for i, j in enumerate(func_list):
    if j == '+':
        t = num_list[i] + num_list[i+1]
        num_list[i] = t
        del num_list[i+1]
        del func_list[i]
    elif j == '-':
        t = num_list[i] - num_list[i+1]
        num_list[i] = t
        del num_list[i+1]
        del func_list[i]
    else:
        break
        

# func_list_fin = []

# for i in func_list:                 #슈발 계산 어케 해 이거
#     if i == '*' or i == '/':
#         func_list
#     elif i == '+' or i == '-':
#         pass
        


total = num_list[0]
if func_list[0] == '=':
    print(total)
elif func_list[0] == '+':
    print(total + num_list[1])
elif func_list[0] == '-':
    print(total - num_list[1])
elif func_list[0] == '*':
    print(total * num_list[1])
elif func_list[0] == '0':
    print(total / num_list[1])

# print(pls_list)
# print(mul_list)
# print(pls_index)
# print(mul_index)



