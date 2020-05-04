# Age calculate
import datetime

# Accepting year from user
birth_year = input('what year were you born?')

# Getting current datetime
now = datetime.datetime.now()
print(type(now.year))

# substrting current year to birth year and birth year converted : str to int
age = now.year - int(birth_year)

# f - formatting string
print(f'Your age is : {age}') 