# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "testerpython65@gmail.com"
PASSWORD = "zwigzayryxdncnou"

PLACEHOLDER = "[NAME]"

data = pandas.read_csv("birthdays.csv")


now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    person_name = birthday_dict[today]
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
    # with the person's actual name from birthdays.csv
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        letter_data = file.read()
        letter_data = letter_data.replace(PLACEHOLDER, person_name["name"])
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL
                            , to_addrs=person_name["email"]
                            , msg=f"Subject:Happy Birthday!\n\n{letter_data}.")









