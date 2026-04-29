from gmail_reader import get_unread_emails
from invoice_parser import extract_invoice_data


def run():
    emails = get_unread_emails()

    for email in emails:
        data = extract_invoice_data(email)
        print(data)


if __name__ == "__main__":
    run()
