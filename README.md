# email_script
This script uses the library yagmail which is used to send emails.
yagmail is a GMAIL/SMTP client that aims to make it as simple as possible to send emails.
For running this script turn on less secured apps access to email
for Help :https://support.google.com/accounts/answer/6010255?hl=en

You cane edit the contents like this

body = 'This is  the body'
html = '<a href="https://github.com/">Click me!</a>'
img = '/local/file/bunny.png'

yag.send(to = to, subject = subject, contents = [body, html, img])



for more details regarding yagmail follow : https://github.com/kootenpv/yagmail
