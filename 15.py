from datetime import datetime

# finding all 1xx6 years where 26 Jan is Monday
for year in range(1016, 1996, 20):
  d = datetime(year, 1, 26)
  if d.weekday() == 0:
    print(year)