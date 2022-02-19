import calendar
i = input().split(" ")
calendar.setfirstweekday(calendar.MONDAY)
day = (calendar.weekday(int(i[2]), int(i[0]), int(i[1])))
print(calendar.day_name[day].upper())
