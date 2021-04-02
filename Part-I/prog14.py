# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

from datetime import date
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
delta =  last_date - first_date
total_days = delta.days
print("Total days between two dates: ",total_days)
print(last_date) # 2014-07-11