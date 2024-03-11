# Birthday Email Sender

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

- **John Smith**
  - **Email:** john.smith@example.com
  - **Birthday:** 3, 11, 1990

- **Alice Johnson**
  - **Email:** alice.johnson@example.com
  - **Birthday:** 12 5, 1985

When you run the script on John Smith's birthday (March 11th), it will send him a personalized birthday email using a randomly chosen template.

(Birthday Format: mm/dd/yyyy)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This script was inspired by the need to automate birthday wishes for friends and family.
- Thanks to the pandas and smtplib libraries for simplifying data handling and email sending in Python.
