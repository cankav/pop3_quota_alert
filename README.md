pop3_quota_alert
================

Simple Python script to detect and alert pop3 quota limit problems.

I use a satellite email system (dovecot+postfix+fetchmail) to make my pop3 email available from multiple devices. It works quite nicely. As a backup mechanism I keep the mail on the original server and download the emails using pop3 later. Keeping backup on the original server eventually depletes the mail disk usage quota.

pop3_quota_alert.py checks the pop3 server for disk usage quota and sends an alert email to the corresponding email account with the correct configuration on the top of the file.

Any suggestions or pull requests are welcome : )
