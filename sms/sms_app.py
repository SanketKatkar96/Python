## Send Email
import smtplib
import imaplib
import email
from email.message import EmailMessage
from email.header import decode_header
from getpass import getpass

SMTP_SERVER = "smtp.gmail.com"
IMAP_SERVER = "imap.gmail.com"



# Login only once
GMAIL = input("Enter your Gmail: ")
APP_PASSWORD = getpass("Enter your Gmail App Password: ")


def send_email():
    receiver = input("Receiver Gmail: ")
    subject = input("Subject: ")
    message = input("Message: ")

    mail = EmailMessage()
    mail["From"] = GMAIL
    mail["To"] = receiver
    mail["Subject"] = subject
    mail.set_content(message)

    try:
        with smtplib.SMTP(SMTP_SERVER, 587) as server:
            server.starttls()
            server.login(GMAIL, APP_PASSWORD)
            server.send_message(mail)

        print("\nEmail sent successfully!")

    except Exception as error:
        print("Sending failed:", error)


def receive_emails():
    try:
        with imaplib.IMAP4_SSL(IMAP_SERVER, 993) as inbox:
            inbox.login(GMAIL, APP_PASSWORD)
            inbox.select("INBOX", readonly=True)

            status, data = inbox.search(None, "ALL")

            if status != "OK" or not data[0]:
                print("No emails found.")
                return

            ids = data[0].split()[-5:][::-1]

            for mail_id in ids:
                status, data = inbox.fetch(mail_id, "(RFC822)")

                if status != "OK":
                    continue

                msg = email.message_from_bytes(data[0][1])

                subject_parts = decode_header(
                    msg.get("Subject", "No subject")
                )
                subject = ""

                for part, encoding in subject_parts:
                    if isinstance(part, bytes):
                        subject += part.decode(
                            encoding or "utf-8",
                            errors="replace"
                        )
                    else:
                        subject += part

                body = ""

                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            if part.get_content_disposition() == "attachment":
                                continue

                            payload = part.get_payload(decode=True)
                            if payload:
                                body = payload.decode(
                                    part.get_content_charset() or "utf-8",
                                    errors="replace"
                                )
                                break
                else:
                    payload = msg.get_payload(decode=True)
                    if payload:
                        body = payload.decode(
                            msg.get_content_charset() or "utf-8",
                            errors="replace"
                        )

                print("\nFrom:", msg.get("From", "Unknown"))
                print("Subject:", subject)
                print("Message:", body[:1000])
                print("-" * 40)

    except Exception as error:
        print("Receiving failed:", error)


while True:
    print("\n===== EMAIL APPLICATION =====")
    print("1. Send Email")
    print("2. Receive Emails")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        send_email()
    elif choice == "2":
        receive_emails()
    elif choice == "3":
        print("Application closed.")
        break
    else:
        print("Invalid choice.")
