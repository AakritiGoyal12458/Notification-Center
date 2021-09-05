##notification software :
##    pip install plyer for notification
##    pip install request
##    pip install bs4 : beautiful soup
## bs4 help to fetch data from html files and xml

from plyer import notification
import requests
from bs4 import BeautifulSoup
def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        timeout=3,#notification after 3 sec
        #app_icon="C:\icon\insta.jpg" #avoid png here
    )

def getdata(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    notifyme("TIKTOK ", "You win 10000000")


        
