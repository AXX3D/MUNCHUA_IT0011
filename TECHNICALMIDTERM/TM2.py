import datetime

year = int(input("Enter year (YYYY): "))
month = int(input("Enter month (MM): "))
day = int(input("Enter day (DD): "))

d = datetime.datetime(year, month, day)

print('{:%B %d, %Y}'.format(d))
