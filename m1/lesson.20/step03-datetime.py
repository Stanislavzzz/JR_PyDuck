from datetime import datetime, date, time, timedelta

#
# now = datetime.now()
# print(type(now))
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.microsecond)


# today = date.today()
# print(type(today))
# print(today)
# print(today.year)
# print(today.month)
# print(today.day)

# t = time(12, 30, 45)
# print(type(t))
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)


# d1 = date(2026, 11, 9)
# d2 = date(2026, 10, 7)
#
# print(d1 < d2)
# print(d1 > d2)
# print(d1 == d2)
#
#
# delta = d1 - d2
# print(delta)


# today = date.today()
# after_7 = today + timedelta(days=7)
# print(after_7)
#
# before_3 = today - timedelta(days=3)
# print(before_3)



# now = datetime.now()
# print(now)
#
# formatted = now.strftime("%Y _ %m _ %d %H / %M / %S")
# print(formatted)


text = "2026_10_07 17-37-37"

dt = datetime.strptime(text, "%Y_%m_%d %H-%M-%S")
print(dt)
print(type(dt))