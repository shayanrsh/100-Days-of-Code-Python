import pandas as pd
import datetime as dt
import random
import smtplib
##################### Extra Hard Starting Project ######################

# replace your email with my_email string
# replace your App Password with password string
my_email = "myEmail@gmail.com"
password = "akmv etgv gwhp mgpe"

# 1. Update the birthdays.csv
birthday_data = pd.read_csv("birthdays.csv")

# 2. Check if date_from matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_year = now.year
today_month = now.month
today_day = now.day

if int(birthday_data.month) == today_month and int(birthday_data.day) == today_day:
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as template_letter:
        letter = template_letter.read()
        letter_with_name = letter.replace("[NAME]", birthday_data.name[0])

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_data.email[0],
                        msg=f"Subject: Happy Birthday!\n\n{letter_with_name}")