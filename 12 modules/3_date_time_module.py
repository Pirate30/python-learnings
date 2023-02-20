import datetime
# contains - year month date day hour minute second microsecond

# getting current date time
print(datetime.datetime.now())

# ----------------------------------------
# strftime - takes params and format simbol and returns formatted date

now = datetime.datetime.now()

print(now.strftime('%D'))  # date
print(now.strftime('%d'))  # day
print(now.strftime('%m'))  # month
print(now.strftime('%y'))  # year 23
print(now.strftime('%Y'))  # year 2023
print(now.strftime('%B'))  # year February
print(now.strftime('%b'))  # year Feb
print(now.strftime('%H'))  # hour in 24 fromat
print(now.strftime('%I'))  # hour in 12 fromat
print(now.strftime('%p'))  # am/pm
