##################### Extra Hard Starting Project ######################
import pandas
import random
import datetime
import smtplib

# Constants
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
MY_EMAIL = "dudesaschaa@gmail.com"
PASSWORD = ""

# 1. Update the birthdays.csv - Done

# 2. Check if today matches a birthday in the birthdays.csv
birthdays_data = pandas.read_csv("birthdays.csv")

for index, row in birthdays_data.iterrows():
    birthday_month = row["month"]
    birthday_day = row["day"]
    email = row["email"]

    now = datetime.datetime.now()
    now_month = now.month
    now_day = now.day

    name = row["name"]

    if birthday_month == now_month and birthday_day == now_day:
        random_letter_path = f"letter_templates/{random.choice(LETTERS)}"
        with open(random_letter_path, mode="r") as letter:
            # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
            # actual name from birthdays.csv
            letter_content = letter.read().replace("[NAME]", name)
            # 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:Happy Birthday\n\n{letter_content}")

