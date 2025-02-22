import smtplib

def send_email(message):
    sender = "your_email@gmail.com"
    password = "your_app_password"
    receiver = "admin@gsmedical.com"
    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, f"Subject: IDS Alert\n\n{message}")