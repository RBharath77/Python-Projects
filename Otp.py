import random, smtplib
from email.mime.text import MIMEText

def send_email(email, otp):
    try:
        msg = MIMEText(f"Your OTP is: {otp}")
        msg["Subject"] = "Order OTP"
        msg["From"] = SENDER
        msg["To"] = email

        with smtplib.SMTP(SMTP_SERVER, 587) as s:
            s.starttls()
            s.login(SENDER, PASSWORD)
            s.sendmail(SENDER, email, msg.as_string())
        print("Email sent!")
    except Exception as e:
        print("Email error:", e)

def confirm_order(email, phone):
    otp = ''.join(random.choice("0123456789") for _ in range(4))
    send_email(email, otp)
    print(f"SMS to {phone}: {otp}")

SMTP_SERVER = "smtp.gmail.com"
SENDER = "yourgmail@gmail.com"
PASSWORD = "your_app_password"

confirm_order("gmail Id to user", "Phone number to user")
