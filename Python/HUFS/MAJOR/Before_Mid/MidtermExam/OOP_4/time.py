import time
import datetime

now = datetime.datetime.now()
print("현재 시간 :", time.time())
print("현재 시간 :", now)
print("오늘 :", datetime.date.today())
print("30초 뒤 :", now + datetime.timedelta(seconds=30))
print("내일 :", now + datetime.timedelta(days=1))

time.sleep(1)
print("현재 시간 :", time.time())