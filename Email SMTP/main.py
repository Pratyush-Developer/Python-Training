import random
import smtplib
import datetime as dt

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 3:
    with open("quotes.txt") as file:
        data = file.readlines()
        random_quote = random.choice(data)
        print(random_quote)

    my_email = "testerpython65@gmail.com"
    password = "zwigzayryxdncnou"

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email
                        , to_addrs="javacoder24@yahoo.com"
                        , msg=f"Subject:Motivational Quote\n\n{random_quote}.")
    connection.close()
