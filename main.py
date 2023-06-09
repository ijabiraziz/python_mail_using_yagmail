import yagmail
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


yag_mail = yagmail.SMTP(user=os.getenv('SENDER_EMAIL'), password=os.getenv(
    'SENDER_EMAIL_PASSWORD'), host='smtp.gmail.com')

recipients = ["ijabiraziz@gmail.com", "jabiraziz430@gmail.com"]
subject = "Welcome to MyFitnessCoach!"
body = ["Welcome to the world of fitness and wellness,"]

yag_mail.send(to=recipients, subject=subject, contents=body)
print("Emails have been sent successfully to the recipients' addresses.")