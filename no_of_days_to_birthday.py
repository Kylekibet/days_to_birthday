#!/usr/bin/python3
import datetime

# Get todays date
dttoday = datetime.date.today()
print("today is {}".format(dttoday))
while True:
    # Get users birtday date.
    bday = input("\nPlease enter you birthday(year-month-day) : ")

    # Check weather user entered date in the formart provided(year-month-day)
    try:
        # Split birtday date into three variables year, month and day.
        year, month, day = bday.split('-')
        break
    except:
        # Prints out incase of errors occured during spliting of bday
        print('Please Enter date in the correct format.\nMake sure you are using python3')
# Converting date enter by user from string to integer
year = int(year)
month = int(month)
day = int(day)

# Creats birthday date form date entered by user
bday = datetime.date(dttoday.year, month, day)

# Calculate how old you are
year_old = dttoday.year - year

# Creates Delta-time for remaining days till birthday
days_remaining = bday - dttoday

# Creates Futher birthday
fbday = datetime.date(dttoday.year+1, month, day)

# Gets Number of days remaining till next year's birthday
days_remaining_to_next_bday = fbday - dttoday

# Conditional statement to check weather birthday has passed or not
if days_remaining.days >= 1:
    print('\n{} days remaining to your birthday. You will turn {}.\n'.format(days_remaining.days,year_old))
elif days_remaining.days == 0:
    print('\nHappy birthday!!! Today you turn {}. CONGRATULATIONS!!!\n'.format(year_old))
else:
    print('\nYou birth day has passed this year. You will turn {} next year.\nDays remaining from today till next birthday is {}\n'.format(year_old + 1, days_remaining_to_next_bday.days))
