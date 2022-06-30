from email import header
import requests
import smtplib
from bs4 import BeautifulSoup
import time

URL = "https://www.bestbuy.com/site/assassins-creed-valhalla-standard-edition-playstation-4-playstation-5/6412166.p?skuId=6412166"
headers = {'User-Agent' :  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')


    title = soup1.find('h1')
    price = soup1.find(class_ = "priceView-hero-price priceView-customer-price").get_text()
    converted_price = float(price[1:3])

    if (converted_price < 35):
        send_mail()
    print(converted_price)
    if (converted_price > 35):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mathew2002raj@gmail.com', 'AuthenticationPassword')

    subject = 'Price fell down!'
    body = 'check the Amazon link: "https://www.bestbuy.com/site/assassins-creed-valhalla-standard-edition-playstation-4-playstation-5/6412166.p?skuId=6412166"'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'mathew2002raj@gmail.com',
        'mathew2002raj@gmail.com',
        msg
    )
    print('Hey Email has been successfully sent')
    server.quit()


while (True):
    check_price()
    time.sleep(86400)



