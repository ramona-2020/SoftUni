from datetime import date, datetime, timedelta

create_date = "2022-07-15 10:00:00"
t_date = datetime.strptime(create_date, "%Y-%m-%d %H:%M:%S")

econt_delivered_date = datetime.strptime("2022-07-04 10:00:00", "%Y-%m-%d %H:%M:%S")

#  (datetime.now() - datetime.strptime(self.econt_delivered, '%Y-%m-%d %H:%M:%S')).days <= 14
days_diff = (datetime.now() - econt_delivered_date).days <= 14
print(days_diff)

# type object 'Datetime' has no attribute 'strptime'