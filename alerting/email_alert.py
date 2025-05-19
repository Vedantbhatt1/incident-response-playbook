import smtplib
from email.mime.text import MIMEText

def send_alert(subject, body):
    sender = "your_email@example.com"
    recipient = "admin@example.com"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = recipient

    try:
        server = smtplib.SMTP("smtp.example.com", 587)
        server.starttls()
        server.login(sender, "your_password")
        server.sendmail(sender, [recipient], msg.as_string())
        server.quit()
        print("[+] Email alert sent.")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")
