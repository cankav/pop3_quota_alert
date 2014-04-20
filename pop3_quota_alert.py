# POP3 quota alert script

# CONFIG ####################################################################

# my mail server does not return mailbox size in pass_ function
# so I set it by hand here in BYTES, number below is 250 MB
MAILBOX_SIZE=250000000

# mail user
USER='can@example.com'

# mail server
SERVER='mail.example.com'

# mail password
PASS='high_security_password_:)'

# send email if mailbox usage is more than more than percentage
ALERT_LIMIT=80

# sensible defaults
ALERT_MAIL_TO=USER
ALERT_MAIL_FROM=USER
ALERT_MAIL_SERVER=SERVER
ALERT_MAIL_SERVER_PORT=587
ALERT_MAIL_USER=USER
ALERT_MAIL_PASS=PASS
#############################################################################

import poplib

M = poplib.POP3(SERVER)
M.user(USER)
M.pass_(PASS)
mb_size = M.stat()[1]

if mb_size / float(MAILBOX_SIZE) * 100 > ALERT_LIMIT:
    import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText( "Quota alert for user " + USER + " in server " + SERVER 
                    + " usage percentage: " 
                    + "%.0f" % float(mb_size / float(MAILBOX_SIZE) * 100) )

    msg['Subject'] = 'Quota alert'
    msg['From'] = ALERT_MAIL_FROM
    msg['To'] = ALERT_MAIL_TO

    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    s = smtplib.SMTP(ALERT_MAIL_SERVER, ALERT_MAIL_SERVER_PORT)
    s.login(ALERT_MAIL_USER, ALERT_MAIL_PASS)
    s.sendmail(ALERT_MAIL_FROM, ALERT_MAIL_TO, msg.as_string())
    s.quit()
