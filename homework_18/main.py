import re
from datetime import datetime


def extract_email_logins(emails):
    return [re.match(r"^([^@]+)", email).group(1) for email in emails]


emails = ["john.doe@gmail.com", "alidin123@yahoo.com", "test_user@msci.org"]
print("1. Логины из email:", extract_email_logins(emails))


def hide_phone_numbers(text):
    return re.sub(r"\d", "*", text)


text_with_phones = "Call me at 123-456-7890 or 987-654-3210"
print("\n2. Скрытые номера:", hide_phone_numbers(text_with_phones))


def extract_hashtags(text):

    return re.findall(r"#\w+", text.lower())


post = "Learning #regex is #fun with #Python3"
print("\n3. Найденные хештеги:", extract_hashtags(post))


def validate_dates(text):
    def is_valid(date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    dates = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", text)
    return [date for date in dates if is_valid(date)]


text_with_dates = "Important dates: 2025-01-01, 2025-13-40, 2024-12-31, 1999-00-10"
print("\n4. дата:", validate_dates(text_with_dates))


if i == "main":

    print("\n=== Результаты  ===")
    print("1.", extract_email_logins(emails))
    print("2.", hide_phone_numbers(text_with_phones))
    print("3.", extract_hashtags(post))
    print("4.", validate_dates(text_with_dates))
