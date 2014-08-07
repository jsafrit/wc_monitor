import requests
import time
from bs4 import BeautifulSoup
from SendMeMail import Mail

#####################################
## user variables
#####################################
camurl = 'http://dl0414.myfoscam.org'
#email = '3013797664@txt.att.net'
email = '3362631393@vtext.com'
checkInterval = 600  #in seconds
retryLimit = 5

def getCamStatus():
    '''Checks status of camera and responds True if reachable'''
    r = requests.get(camurl + '/login_user.htm')
    soup = BeautifulSoup(r.content)
    return bool(len(soup.find_all('input', attrs={'id':'login_user'})))

def sendNotification(mailer,cnt):
    '''Send e-mail/text notification of failure'''
    msg = 'Your remote camera could not be reached. (try #%d)' % cnt
    print msg, 
    mailer.setMessage(msg)
    mailer.send()
    

def main():
    mailer = Mail(toaddr=email, subject='Camera Monitor')
    warnCnt = 0
    
    while True:
        cam_up = getCamStatus()

        if not cam_up:
            warnCnt += 1
            #send a notificaion
            sendNotification(mailer, warnCnt)
            #exit before flooding
            if warnCnt >= retryLimit:
                break
            #retry sooner since we failed
            time.sleep(checkInterval/10)

        else:
            #reset warnings
            warnCnt = 0
            #wait for defined interval before checking again
            time.sleep(checkInterval)


if __name__ == '__main__':
    main()

