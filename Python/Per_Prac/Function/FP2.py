# def AllAdd(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result

# Ask = input()
def AllAdd(*args):
    result = 0
    for i in args:
        result += i
    return result

# 사용자로부터 '1, 4, 5, 3, 2' 형태의 문자열을 입력받습니다.
Ask = input("숫자들을 콤마(,)로 구분하여 입력하세요: ")

# 1. 입력받은 문자열을 콤마(,)를 기준으로 잘라 리스트로 만듭니다.
#    결과: ['1', ' 4', ' 5', ' 3', ' 2']
numbers_str = Ask.split(',')

# 2. 리스트의 각 문자열 요소를 정수(int)로 변환합니다.
#    map() 함수와 int를 사용하여 각 요소를 정수로 바꿔줍니다.
#    결과: [1, 4, 5, 3, 2]
numbers = list(map(int, numbers_str))

# 3. AllAdd 함수를 호출할 때 리스트 앞에 *를 붙여줍니다.
#    이는 리스트의 모든 요소를 각각의 인자(argument)로 풀어 전달하라는 의미입니다.
#    AllAdd(1, 4, 5, 3, 2)와 같이 호출하는 것과 동일한 효과를 냅니다.
total = AllAdd(*numbers)

# 최종 결과를 출력합니다.
print(f"입력한 모든 숫자의 합은 {total}입니다.")