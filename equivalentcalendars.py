import calendar

def sameyear(year1, year2):
    check1 = calendar.weekday(year1, 1, 1) == calendar.weekday(year2, 1, 1)
    check2 = calendar.weekday(year1, 12, 31) == calendar.weekday(year2, 12, 31)
    return True if check1 and check2 else False

def genlists(yearlb, yearub):
    buckets = [[yearlb]]
    for year in [x for x in range(yearlb+1, yearub+1)]:
        placed = False
        for bucket in buckets:
            if sameyear(bucket[0], year):
                bucket.append(year)
                placed = True
        if placed == False:
            buckets.append([year])
    return buckets

def findcalendars(year, yearlb, yearub):
    buckets = genlists(yearlb, yearub)
    years =[]
    for bucket in buckets:
        if year in bucket:
            years = bucket
    return years

#print groups of years that can share calendar (1900-2100)
calendars = genlists(1900, 2100)
for cal in calendars:
    print(cal)

#print list of years that have same calendar as 2019 (1900-2100)
print('\n')
print('Calendar years that can be used for 2019:')
print(findcalendars(2019, 1900, 2100))
