import os, smtplib
from email.message import EmailMessage

EMAIL = os.environ.get('')
PASSWORD = os.environ.get('')
'''lines = open('.../cc@home/contact_infoII.txt', 'r+')
for line in lines:
    name = line.split(',')[0]
    email = line.split(',')[1]'''
try:
    msg = EmailMessage()
    msg['Subject'] = '#CarpentryConHome Session Feedback'
    msg['From'] = EMAIL
    msg['To'] = 'ousodaniel@gmail.com'
    msg.set_content('''
    Dear {},

    Thank you for participating in week one sessions of the #CarpentryConHome (https://twitter.com/search?q=%23CarpentryConHome&src=typed_query). As is custom, we would love to listen to you through your feedback for the sessions you attended. Kindly, advance the Carpentries cause by taking a few minutes completing the feedback form (https://carpentries.typeform.com/to/K8dXnKHL).

    We hope to reconnect with you in subsequent sessions for the remaining weeks; you may bookmark the schedule (https://2020.carpentrycon.org/schedule/).

    Best regards,
    Ouso
    On behalf of the CarpentryConHome Taskforce.
    '''.format(name))
    msg.add_alternative('''\
    <html>
       <head>
          <p>Dear {},</p>
       </head>
       <body>
          <p>Thank you for participating in week one sessions of the <a href="https://twitter.com/search?q=%23CarpentryConHome&src=typed_query">#CarpentryConHome</a>. As is custom, we would love to listen to you through your feedback for the sessions you attended. Kindly, advance the Carpentries cause by taking a few minutes completing the feedback <a href="https://carpentries.typeform.com/to/K8dXnKHL">form</a>.<br><br>
            We hope to reconnect with you in subsequent sessions for the remaining weeks; you bookmark the <a href="https://2020.carpentrycon.org/schedule/">schedule</a>.<br><br>Best regards,<br>Ouso<br>On behalf of the CarpentryConHome Taskforce.
            </p>
       </body>
    </html>'''.format(name), subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)
    print('An email has been sent to {} at: {}!'.format(name, email))
except: print('Failed to send email to {}!!!'.format(name))

