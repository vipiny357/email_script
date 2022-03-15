import yagmail
yag = yagmail.SMTP('abc123@gmail.com','password')
# yag = yagmail.SMTP('SENDERS EMAIL', 'Password')

receiver="xyz123@gmail.com"
# receiver="Recievers Emails"

body="test bodyyy"
# body="body of the email"

filename= r'C:/Users/Vipin Kumar Yadav/Desktop/email script/tunhi/Jazmin Ulyatt.pdf'
# filename= r'path of the file to send as attachment'

sub="Certificate of participation"
# sub = "subject of the email"

yag.send(
    to=receiver,
    subject=sub,
    contents=body, 
    attachments=filename,
)