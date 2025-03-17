#----------------------Extra Hard Starting Project -------------------------

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and,
# replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import pandas as pd
import datetime as dt
import random

OLD_TEXT = "[NAME]"
my_email = 'leonpython4@gmail.com'  # my email
password = 'ivdsozifvrojgmdy'

# import the birthday.csv
data = pd.read_csv('birthdays.csv')
name_list = data.to_dict(orient='records')

# current day and month
now = dt.datetime.now()
current_day = now.day
current_month = now.month

for name in name_list:
    birth_date = dt.datetime(year=name['year'], month=name['month'], day=name['day'])
    day = birth_date.day
    month = birth_date.month

    if current_day == day and current_month == month:
        email = name['email']
        pick_letter = random.randint(1, 3)
        with open(f"letter_templates/letter_{pick_letter}.txt") as file:
            content = file.read()
            birth_wish = content.replace(OLD_TEXT, name['name'])

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject:Happy Birthday!\n\n{birth_wish}")
