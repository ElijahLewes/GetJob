from email.message import EmailMessage



def send_email(to_addr: str, subject: str, body: str) -> None:
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "no-reply@example.com"
    msg["To"] = to_addr
    msg.set_content(body)

    # Placeholder: print instead of sending
    print(f"Sending email to {to_addr}: {subject}")
