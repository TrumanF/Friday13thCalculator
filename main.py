from collections import deque

days = deque(['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'])
unordered_days = days.copy()


def generateCalendar(starting_day, leap_year=False):
    months = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31,
              'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31,
              'Nov': 30, 'Dec': 31}
    if leap_year:
        months['Feb'] += 1
    starting_day = unordered_days.index(starting_day)
    print("Starting day: {0}".format(starting_day))
    last_day = starting_day - 1 if starting_day != 0 else 6
    print(last_day)
    days.rotate(-starting_day)
    friday13Count = 0
    for month in months:
        for count, _ in enumerate(unordered_days):
            if count != 3:
                print("%-3s" % "-", end=" ")
            else:
                print("%-3s" % month, end=" ")
        print()
        for day in unordered_days:
            print("%-3s" % day, end=" ")
        print()
        for i in range(months[month]):
            if month != 'Jan' and i == 0:
                day_index = last_day + 1 if last_day != 6 else 0
            else:
                day_index = (i + (last_day + 1)) % 7

            if i == 0 and day_index != 0:
                for _ in range(day_index):
                    print("%-3s" % " ", end=" ")
            if day_index != 6:
                print("%-3d" % (i + 1), end=" ")
            else:
                print(i + 1)

            if i == months[month] - 1:
                last_day = day_index

            if i == 12 and day_index == 5:
                friday13Count += 1
        print()
    print("\n \n \n")
    return friday13Count


maxCount = (0, "")
listCount = []
for day in unordered_days:
    print("Starting day: {0}".format(day))
    currentCount = generateCalendar(day)
    if currentCount > maxCount[0]:
        maxCount = (currentCount, day)
    listCount.append(currentCount)
    print("Count: {0}".format(currentCount))
print(maxCount)
print(listCount)
