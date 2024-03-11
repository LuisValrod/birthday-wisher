
import pandas as pd
import datetime as dt
from random import choice
import smtplib
# 1. Update the birthdays.csv
data = pd.read_csv('birthdays.csv')
data.drop(index=1, inplace=True)
data.drop(index=0, inplace=True)
print(data)
dContacts = {
    'name': ['Luis Rodriguez', 'Luis Valrod', 'Conchi Perez', 'Luis Invento', 'Luis Gmail'],
    'email': ['luisrodriguezvalido@gmail.com', 'lvalrod@yahoo.com', 'phconchi@yahoo.es', 'luis_skull711@hotmail.com', 'lvalrod87@gmail.com'],
    'year': [1987, 1987, 1979, 1950, 1949],
    'month': [12, 3, 6, 3, 3],
    'day': [3, 11, 5, 11, 11]
}
dfContacts = pd.DataFrame(dContacts)
data = data._append(dfContacts, ignore_index=True)
print(data)
data.to_csv('birthdays2.csv', index=False)

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
currentDay = now.day
currentMonth = now.month

lst_rec= []
for n in range(len(dfContacts['year'])):
    if dfContacts['month'][n] == currentMonth and dfContacts['day'][n] == currentDay:
        lst_rec.append({'name': dfContacts['name'][n],
                        'email': dfContacts['email'][n]})
print(lst_rec)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
lst_choices = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
rchoice = choice(lst_choices)
with open(f'./letter_templates/{rchoice}') as ldata:
    letter = ldata.read()

letters = [letter.replace('[NAME]', lst_rec[n]['name']) for n in range(len(lst_rec))]
print(letters)
# 4. Send the letter generated in step 3 to that person's email address.

my_email = 'lvalrod87@gmail.com'
my_password = 'umzc lald manl gdga'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    for n in range(len(lst_rec)):
        connection.sendmail(
            from_addr=my_email,
            to_addrs=lst_rec[n]['email'],
            msg=f'Subject: Happy Birthday!! \n\n {letters[n]}'
        )




