import math
import random

#[문제1] 사과상자 및 남은 과일 개수
사과 = 1200
상자크기 = 36
print(f'{사과 // 상자크기}상자와 나머지 {사과 % 상자크기}개')

#[문제2] 원의 넓이
radius = int(input())
print(f'{radius ** 2 * math.pi:.2f}')

#[문제3] 함수식
x, a, b = 3, 5, 7
total = x ** 2 + b/a*x + (b/(a*2)) ** 2
print(total)

#[문제4] 영화 나이 제한 검사
age = int(input())

if age >= 15:
    print("영화를 보실 수 있습니다")
else:
    print("이 영화를 보실 수 없습니다.")

#[문제5] 구게임 게임
option = ["왼쪽", "중앙", "오른쪽"]
com = random.choice(option)
user = input("어디로 공을 차겠어요?(왼쪽, 중앙, 오른쪽)")

if user == com:
    print("수비성공")
else:
    print("패널티킥 성공")