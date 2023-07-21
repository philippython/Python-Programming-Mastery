import os
import imghdr
from dotenv import load_dotenv
from smtplib import SMTP, SMTP_SSL
from email.message import EmailMessage
from datetime import datetime

load_dotenv()

name = "philip"
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
# receipents = [EMAIL_ADDRESS, "test@gmail.com"]
email_body = """"
Hello, I hope this meessage meets you well, I'm reminding you of the standuo meeting scheduled for 9:00am 

Sincerely,
Philip
"""

msg = EmailMessage()
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg["Subject"] = "Standup Meeting Reminder"
msg.set_content(email_body)
# server = SMTP("smtp.gmail.com", 587)
# server.ehlo()
# server.starttls()
# server.quit()

# images = ["final code\sky_diving 2.jpg", "final code\sky_diving.jpg"]

# for image in images :
#     with open(image, "rb") as file:
#         image_file = file.read()
#         file_name = file.name
#         file_format = imghdr.what(file_name)
    
#     msg.add_attachment(image_file, maintype="image", subtype=file_format, filename = file_name)    

# with open(r"final code\odulaja philip temitayo.pdf", "rb") as file:
#         pdf_file = file.read()
#         file_name = file.name

# msg.add_attachment(pdf_file, maintype="application", subtype="octet-stream", filename=file_name)

with SMTP_SSL("smtp.gmail.com", 465) as server:
    # server.ehlo()
    # server.starttls()
    # server.ehlo()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    if datetime.now().hour == 8 and datetime.now().minute == 30 and datetime.now().weekday() == 0:
        server.send_message(msg)
        print("reminder sent")
    else:
        print("Time isn't")


    # 0 - m, t -1, w -2, t-3, f -4, s -5, s -6
    # print(datetime.now().weekday())
    # if datetime.now().weekday() == 6 :
    #     print("Today is friday, mail would be sent")
    #     server.send_message(msg)
    #     print("Email sent")
    # else:
    #     print("Today is not friday!")
    # server.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=EMAIL_ADDRESS, msg="Subject : Testing Email\n\nHello is this working?")


# print(datetime.now())
# print(datetime.today())
# print(datetime.now().time())
# print(datetime.now().month)
# print(datetime.now().day)
# print(datetime.now().year)
# print(datetime.now().date())

# birthday = datetime(2004, 5, 26)
# print(birthday)
