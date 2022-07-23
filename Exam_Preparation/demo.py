from datetime import datetime, timedelta

date_from = datetime.strptime('2022-08-01', '%Y-%m-%d')
date_end = datetime.strptime('2022-07-18', '%Y-%m-%d')

print(date_from - date_end)
print(date_end + timedelta(days=14))
