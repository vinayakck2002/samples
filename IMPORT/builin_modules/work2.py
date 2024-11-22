import datetime
date=datetime.datetime.now()
print(date)
print(date.strftime('%x'))#11/22/24
print(date.strftime('%A'))#Friday -day full version
print(date.strftime('%B'))#November -month version
print(date.strftime('%Y'))#2024 - year with century