#  https://www.youtube.com/watch?v=pdy3nh1tn6I&list=PLnbmk43t7uQM5BQT_C2rXqUKanK0dwOkV&index=102

from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'mavericos1@abv.bg'
email_password = 'k0nstantina'

email_recever = 'mavericos2@abv.bg'

subject = "Ko staaa"
body = """ Shtom go 4etesh zna4i e minalo
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_recever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_recever, em.as_string())
