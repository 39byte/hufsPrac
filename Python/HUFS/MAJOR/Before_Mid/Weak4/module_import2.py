import random
import time
import math

data_list = []
i = 0
str_time = time.time()

# while i <= 1000000:
#     i += 1
#     a = random.randint(1, 1000000)
#     data_list.append(a)

# for i in range(1000000):
#     a = random.randint(1, 1000000)
#     data_list.append(a)

data_list = [random.randint(1, 1000000) for i in range(1000000)]

fin_time = time.time()
total = fin_time - str_time
print(f'생성 소요 시간 : {total:.8f}')

str_time = 0; fin_time = 0
str_time = time.time()
sorted(data_list)
fin_time = time.time()
total = fin_time - str_time
print(f'정렬 소요 시간 : {total:.8f}')

str_time = 0; fin_time = 0
str_time = time.time()
x = (1, 3)
y = (3, 2)
dis = math.sqrt((x[0] - y[0])**2 + (x[1]-y[1])**2)
fin_time = time.time()
total = fin_time - str_time
print(f'계산 시간 : {total:.8f}')