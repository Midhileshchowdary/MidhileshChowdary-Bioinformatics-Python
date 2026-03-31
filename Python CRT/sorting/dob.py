'''sort a list of dates provided in DD-MM-YYYY format chronologically'''
def is_valid_date(date_str):
    if len(date_str) != 10 or date_str[2] != '-' or date_str[5] != '-':
        return False
    d = date_str[0:2]
    m = date_str[3:5]
    y = date_str[6:10]
    if not (d.isdigit() and m.isdigit() and y.isdigit()):
        return False
    day = int(d)
    month = int(m)
    year = int(y)
    if month < 1 or month > 12:
        return False
    if month == 2:
        if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            max_day = 29
        else:
            max_day = 28
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 31
    if day < 1 or day > max_day:
        return False
    return True
def parse_date(date_str):
    parts = date_str.split('-')
    day = int(parts[0])
    month = int(parts[1])
    year = int(parts[2])
    return year,month,day
def sort_dates(dates):
    n = len(dates)
    for i in range(n):
        for j in range(0, n - i - 1):
            if parse_date(dates[j]) > parse_date(dates[j + 1]):
                temp = dates[j]
                dates[j] = dates[j + 1]
                dates[j + 1] = temp
    return dates
n=int(input("Number of dates"))
dates=[]
for i in range(n):
    temp=input(f"Enter the {i+1} date : ")
    dates.append(temp)
sorted_dates=sort_dates(dates)
print(sorted_dates)
