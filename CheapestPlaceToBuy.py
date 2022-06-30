from email import header
import requests
import smtplib
from bs4 import BeautifulSoup
import time

#bestBuy
#walMart
#target
#Costco
#Amazon
URL = "https://www.bestbuy.com/site/assassins-creed-valhalla-standard-edition-playstation-4-playstation-5/6412166.p?skuId=6412166"

headers = {'User-Agent' :  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

def find_cheapest_price():
    pageBestBuy = requests.get(URL, headers = headers)

    soupBestBuy = BeautifulSoup(pageBestBuy.content, 'html.parser')


    title = soupBestBuy.find('h1')
    priceBestBuy = soupBestBuy.find(class_ = "priceView-hero-price priceView-customer-price").get_text()
    allPrices = []
    converted_price = float(priceBestBuy[1:3])

    if (converted_price < 35):
        send_mail()
    print(converted_price)


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


find_cheapest_price()




