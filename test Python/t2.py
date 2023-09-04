day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day, month, year):
    if is_leap(year):
        day_in_month[2] = 29
    else:
        day_in_month[2] = 28
    return sum(day_in_month[:month]) + day

def day_in_year(day, month, year):
    if is_leap(year):
        day_in_month[2] = 29
    else:
        day_in_month[2] = 28
    return day_in_month[month] - day_of_year(day, month, year)

def date_diff(date1, date2):
    day1, month1, year1 = date1.split('-')
    day2, month2, year2 = date2.split('-')
    return abs(day_of_year(int(day1), int(month1), int(year1)) - day_of_year(int(day2), int(month2), int(year2)))

print(date_diff('01-01-2018', '01-01-2020')) 