def Alladd(*args):
    result = 0
    for i in args:
        result += i
    return result

FAsk = input("입력을 콤마(,)로 구분하여 입력하세요.\n")
commiz = FAsk.split(',')
askstr = list(map(int, commiz))
total = Alladd(*askstr)

print(f'최종값은 {total}입니다.')