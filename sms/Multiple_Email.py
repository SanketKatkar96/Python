
import smtplib
import ssl
from email.message import EmailMessage
from getpass import getpass

sender = input("Enter your Gmail: ").strip()
password = getpass("Enter your Gmail App Password: ").strip()

receivers = input(
    "Enter receiver emails separated by commas: "
).split(",")

subject = input("Enter email subject: ")
message = input("Enter your message: ")

try:
    context = ssl.create_default_context()

    with smtplib.SMTP(
        "smtp.gmail.com", 587, timeout=30
    ) as server:

        print("Starting TLS...")
        server.starttls(context=context)

        print("Logging into Gmail...")
        server.login(sender, password)

        print("Login successful!")

        for receiver in receivers:
            receiver = receiver.strip()

            if not receiver:
                continue

            email = EmailMessage()
            email["From"] = sender
            email["To"] = receiver
            email["Subject"] = subject
            email.set_content(message)

            server.send_message(email)
            print("Email sent successfully to:", receiver)

    print("All emails processed.")

except (smtplib.SMTPException, OSError) as e:
    print("Email sending failed:", type(e).__name__)
    print("Details:", str(e))
