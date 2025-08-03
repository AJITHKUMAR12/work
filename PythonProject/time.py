import time
import smtplib
epc=time.time()
print(epc)
localtime=time.localtime(epc)
print(localtime)
smtp=smtplib.SMTP('smtp.gmail.com',587)
smtp.ehlo()
smtp.starttls()
smtp.login('ajithpalaniappan98@gmail.com','Ajith@123')
smtp.sendmail('ajithpalaniappan98@gmail.com','ajithkumar7014@gmail.com',"Hello World")
smtp.quit()