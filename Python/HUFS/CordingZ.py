print("숫자를 입력해주세요.")
a = int(input()); b = int(input()); c = int(input())
cm_list = [a, b, c]
cm_list.sort()

if cm_list[2] >= cm_list[0] + cm_list[1]:
    print("Invalid")
elif cm_list[0] == cm_list[1] == cm_list[2]:
    print("Equilateral")
elif (cm_list[0] == cm_list[1]) or (cm_list[1] == cm_list[2]):
    print("Isosceles")
elif cm_list[0] != cm_list[1] != cm_list[2]:
    print("Scalene")