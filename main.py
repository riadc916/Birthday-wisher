##################### Normal Starting Project ######################
import datetime as dt
import random
import smtplib
from importlib.resources import contents
import os
  

now=dt.datetime.now()
today=(now.month,now.day)

# HINT 2: Use pandas to read the birthdays.csv
import pandas as pd
read_csv=pd.read_csv("birthdays.csv")


birthday_dict={
    (data_row.month,data_row.day): data_row for (index,data_row) in read_csv.iterrows()
}


if today in birthday_dict:
    birthday_person=birthday_dict[today]
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    MY_EMAIL = os.environ.get("MY_EMAIL")
    MY_PASSWORD = os.environ.get("MY_PASSWORD")
    with open(file_path,"r") as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject: Happy Birthday!\n\n{contents}")


