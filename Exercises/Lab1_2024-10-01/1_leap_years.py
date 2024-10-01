from calendar import day_name, isleap, weekday

cur = 2025
while not isleap(cur):
  cur += 1
print("Next leap year:", cur)

print("Leap year between 2000-2051:", len([True for year in range(2000, 2051) if isleap(year)]))

print("July 29, 2016:", day_name[weekday(2016, 7, 29)])
