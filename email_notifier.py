import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, body):
    from_email = "Youremail"  # Replace with your email
    password = "YourPassword"      # Replace with your app password

    # Create the email
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["corey.gregg@gmail.com"] = to_email

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(from_email, password)
        server.send_message(msg)

# Test it
if __name__ == "__main__":
    send_email("test@example.com", "Test Subject", "This is a test email!")