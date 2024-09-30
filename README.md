# 🎉 Birthday Wisher 🎉
The Birthday Wisher project sends personalized birthday wishes via email. The script reads a CSV file with birthdays, selects a random letter template, and sends an lovely birthday wish email if today matches a birthday.So, no need to remember all those dates!🎂

## 🚀 Features
* Automated Birthday Emails: Sends emails to your friends on their birthdays based on data from a CSV file.<br>
* Randomized Email Templates: Chooses a random template from a folder of .txt files for variety.<br>
* Personalized Messages: Replaces placeholders in the template with the recipient's name for a personalized touch.<br>

## 🛠️ Technologies Used
* Python: Core language for the script.<br>
* pandas: For handling the CSV birthday list.<br>
* datetime: To get today's date and compare it with the birthdays.<br>
* random: To pick a random email template.<br>
* smtplib: To send emails using SMTP.<br>
* os: For handling file paths and loading random templates.<br>

## 📖 How It Works
* Check for Today's Birthday: The script compares the current date with each birthday entry in the birthdays.csv file.<br>
* Send Email: If there's a birthday match, it picks a random birthday message and sends it using your email via SMTP.<br>
* Customization: You can modify both the content of the email (via the templates) and the list of potential birthday wishes.<br>
