import mailbox
import os
from email.message import EmailMessage


def main():
    legit_path = 'legitimate'
    phishing_path = 'phishing'
    output_path = "swapped"

    legit = mailbox.mbox(legit_path)
    phishing = mailbox.mbox(phishing_path)
    output = mailbox.mbox(output_path, create=True)


    num_emails = min(len(legit), len(phishing))

    for i in range(num_emails):
        legit_email = legit[i]
        phishing_email = phishing[i]

        legit_body = getPayload(legit_email)
        phishing_body = getPayload(phishing_email)
        legit_email.set_payload(phishing_body, charset="utf-8")

        output.add(legit_email)

    legit.close()
    phishing.close()
    output.flush()
    output.close()

def should_decode(message):
    if message.get('content-transfer-encoding') in ('base64', 'quoted-printable'):
        return True
    if message.get_content_maintype() == 'text':
        return False
    if message.get_content_maintype == 'multipart':
        return False

def getPayload(message):
    content = ''
    if message.is_multipart():
        for part in message.get_payload(decode=should_decode(message)):
            content = content + str(part.get_payload(decode=should_decode(part)))
    else:
        content = str(message.get_payload(decode=should_decode(message)))
    return content

if __name__ == "__main__":
    main()
