import smtplib
import datetime as dt
import random
import pandas


# Variables
now = dt.datetime.now()
data = pandas.DataFrame()
my_email = "dudesaschaa@gmail.com"
password = ""

# Check if today is a Tuesday and send a random motivational quote
if now.weekday() == 1:
    with open("quotes.txt", "r") as quotes:
        quotes_list = quotes.readlines()
        random_quote = random.choice(quotes_list)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="sash.baschera@gmail.com",
                msg=f"Subject:Your Motivational Quote for this awesome Monday\n\n{random_quote}"
            )


