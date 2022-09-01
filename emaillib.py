import yagmail

def yagSend(subject, contents):
    yag = yagmail.SMTP(user='elppitemp@gmail.com', password='ELPh4rm4cy')
    yag.send(to='mail@eastlindfieldpharmacy.com.au', subject=subject, contents=contents)
