from datetime import datetime
class BirthCal:
    def __init__(self, name, id):
        self.cur_year = datetime.today().year
        self.cur_month = datetime.today().month
        self.cur_day = datetime.today().day
        self.id = id
        self.name = name

    def birth(self):
        # 주민번호 유효성 검증
        if len(self.id) != 8:
            raise ValueError("유효하지 않은 번호입니다.")
        
        # 세기 검증
        if self.id[7] == '1' or self.id[7] == '2': self.year = "19" + id[:2]
        elif self.id[7] == '3' or self.id[7] == '4':  self.year = "20" + id[:2]
        else:
            raise ValueError("유효하지 않은 번호입니다.")
        
        # 월 저장
        if self.id[2] != '0': self.mon = self.id[2:4]
        else: self.mon = id[3]

        # 일 저장 
        if self.id[4] != '0': self.day = self.id[4:6]
        else: self.day = self.id[5]

        # 나이 계산
        self.age = self.cur_year - int(self.year) + 1
        if int(self.mon) <= self.cur_month:
            if int(self.day) <= self.cur_day:
                real_age = self.age - 1
            else: real_age = self.age - 2
        else: real_age = self.age - 2


        print(f"{self.name}님은 {self.year}년 {self.mon}월 {self.day}일에 태어난 {self.age}살(만 {real_age}살)이군요.")
    
human1 = BirthCal("한지원", "060102-3")
human1.birth()
# cur_year = datetime.today().year
# cur_month = datetime.today().month
# cur_day = datetime.today().day

# id = input("주민번호의 뒷 번호 첫 째 자리까지 입력해주세요. (000000-0******)\n")

# if id[7] == '1' or id[7] == '2': year = "19" + id[:2]
# else:  year = "20" + id[:2]
    
# if id[2] != '0': mon = id[2:4]
# else: mon = id[3]

# if id[4] != '0': day = id[4:6]
# else: day = id[5]

# age = cur_year - int(year) + 1
# if int(mon) <= cur_month:
#     if int(day) <= cur_day:
#         real_age = age - 1
#     else: real_age = age - 2
# else: real_age = age - 2

# print(f"당신은 {year}년 {mon}월 {day}일에 태어난 {age}살(만 {real_age}살)이군요.")