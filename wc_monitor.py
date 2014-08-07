import requests
import time
from bs4 import BeautifulSoup

snapurl = 'http://dl0414.myfoscam.org/login_user.htm'
#userauth = ('user1', 'pw1')


while True:
    r = requests.get(snapurl) #, auth=userauth)
    soup = BeautifulSoup(r.content)

    cam_up = len(soup.find_all('input', attrs={'id':'login_user'}))

    if not cam_up:
        #send warning
        print '\nCamera not responding! Sending message...'
    else:
        print '.'
        time.sleep(6)
    


