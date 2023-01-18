from datetime import datetime

for year in range(1016, 1996, 20):
  d = datetime(year, 1, 26)
  if d.weekday() == 0:
    print(year)