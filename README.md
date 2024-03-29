# Birthday Wisher

This Python script automates the process of sending birthday emails to contacts listed in a CSV file. It picks random birthday letter templates, replaces placeholders with recipients' names, and sends personalized emails to each contact.

## Features

- Automatically checks if today matches any birthday in the contact list.
- Sends personalized birthday emails using randomly selected letter templates.
- Supports easy customization of email templates and contact list.

## Dependencies

- Python 3
- pandas
- smtplib

## Installation
```bash
git clone https://github.com/LuisValrod/birthday-wisher.git
```

## Usage

- Update the birthdays.csv file with the contact details. Ensure it includes columns for name, email, year, month, and day.
- Run the script:
```bash
python main.py
```
- The script will check if today is anyone's birthday. If so, it will send a personalized birthday email to each contact.

## Configuration

- Contact List: Update the birthdays.csv file with the details of your contacts.
- Email Templates: Customize the email templates in the letter_templates directory.
- Sender Email: Provide your email address and password in the script for sending emails.

## Example

Suppose you have the following contact list in `birthdays.csv`:

| Name              | Email                     | Year | Month | Day |
|-------------------|---------------------------|------|-------|-----|
| John Smith        | Johny@example.com         | 1987 | 12    | 3   |
| Alby Hammad       | Alhammad@example.com      | 1982 | 3     | 11  |
| Courtney Dohmas   | cdohmas29@example.com     | 1929 | 5     | 11  |
| Alastair Goodlove | goodlove_al93@example.com | 1993 | 3     | 11  |

When you run the script, it will send personalized birthday emails based on the information provided in the `birthdays.csv` file.

(Birthday Format: mm/dd/yyyy)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This script was inspired by the need to automate birthday wishes for friends and family.
- Thanks to the pandas and smtplib libraries for simplifying data handling and email sending in Python.
