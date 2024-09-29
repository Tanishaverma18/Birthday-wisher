import pandas
import datetime as dt
import random
import smtplib
import os

my_email = "Your_email"
password = "Your_password"

#------------ Select Random txt file----------------------#
directory = 'letter_templates'
txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]
random_file = random.choice(txt_files)
random_file_path = os.path.join(directory, random_file)
with open(random_file_path, 'r') as file:
    content = file.read()

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birthday_file = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row['month'], row['day']): f"{row['name']}, {row['email']}, {row['year']}, {row['month']}, {row['day']}" for (index, row) in birthday_file.iterrows()}

#--------------------Send Email Letter------------------------------#

if today in birthdays_dict:
    value = birthdays_dict[today]
    name = value.split(",")[0]
    email = value.split(",")[1]
    personalized_letter = content.replace("[NAME]", name)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email , password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
            )        