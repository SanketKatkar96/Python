
import secrets
import time
import hashlib
import hmac
from getpass import getpass

users = {}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register():
    email = input("Enter your email: ").strip().lower()

    if email in users:
        print("Email already registered!")
        return

    password = getpass("Create password: ")

    if len(password) < 8:
        print("Password must contain at least 8 characters.")
        return

    users[email] = hash_password(password)
    print("Registration successful!")


def login():
    email = input("Enter your email: ").strip().lower()
    password = getpass("Enter your password: ")

    if email in users and hmac.compare_digest(
        users[email], hash_password(password)
    ):
        print("Login successful!")
    else:
        print("Invalid email or password.")


def forgot_password():
    email = input("Enter your registered email: ").strip().lower()

    if email not in users:
        print("Account not found.")
        return

    # Generate a six-digit OTP
    otp = f"{secrets.randbelow(1000000):06d}"
    expiry_time = time.time() + 300  # Expires in 5 minutes

    # Demo only: OTP is displayed in the terminal
    print("Your OTP is:", otp)

    for attempt in range(3):
        entered_otp = input("Enter OTP: ").strip()

        if time.time() > expiry_time:
            print("OTP expired. Try again.")
            return

        if hmac.compare_digest(entered_otp, otp):
            new_password = getpass("Enter new password: ")

            if len(new_password) < 8:
                print("Password must be at least 8 characters.")
                return

            confirm_password = getpass("Confirm new password: ")

            if new_password != confirm_password:
                print("Passwords do not match.")
                return

            users[email] = hash_password(new_password)
            print("Password reset successful!")
            return

        print("Incorrect OTP!")

    print("Too many attempts. Please try again later.")


def main():
    while True:
        print("\n===== PASSWORD RESET SYSTEM =====")
        print("1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
