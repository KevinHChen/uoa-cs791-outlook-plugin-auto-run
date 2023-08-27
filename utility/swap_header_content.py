import mailbox
import os
from email.message import EmailMessage
from email.header import Header


def main():
    legit_path = 'legitimate'
    phishing_path = 'phishing'
    legit_head_phishing_body_path = "legit_head_phishing_body"
    phishing_head_legit_body_path = "phishing_head_legit_body"

    legit_mbox = mailbox.mbox(legit_path)
    phishing_mbox = mailbox.mbox(phishing_path)
    legit_head_phishing_body_mbox = mailbox.mbox(legit_head_phishing_body_path, create=True)
    phishing_head_legit_body_mbox = mailbox.mbox(phishing_head_legit_body_path, create=True)


    num_emails = min(len(legit_mbox), len(phishing_mbox))

    for i in range(num_emails):
        legit_message = legit_mbox[i]
        phishing_message = phishing_mbox[i]
        swap(legit_message, phishing_message, 'Subject')
        swap(legit_message, phishing_message, 'Date')
        swap(legit_message, phishing_message, 'From')
        swap(legit_message, phishing_message, 'To')

        phishing_head_legit_body_mbox.add(legit_message)
        legit_head_phishing_body_mbox.add(phishing_message)

    legit_mbox.close()
    phishing_mbox.close()
    phishing_head_legit_body_mbox.flush()
    legit_head_phishing_body_mbox.flush()
    phishing_head_legit_body_mbox.close()
    legit_head_phishing_body_mbox.close()

def swap(m1, m2, key):
    v1 = m1.get(key)
    v2 = m2.get(key)
    if v1 is not None:
        m1.replace_header(key, v2)
    if v2 is not None:
        m2.replace_header(key, v1)

if __name__ == "__main__":
    main()
