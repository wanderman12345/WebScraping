from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import sys
import smtplib


#Returns the price of an item

def searchItem(item):

    out = {}
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driverCraig = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.bestbuy.com/")
    driverCraig.get("https://sfbay.craigslist.org/")

    try:
        searchCraig = driverCraig.find_element(By.ID, "query")
        searchCraig.send_keys(item)
        searchCraig.send_keys(Keys.RETURN)
        time.sleep(5)
        search = driver.find_element(By.ID, "gh-search-input" )
        search.send_keys(item)
        search.send_keys(Keys.RETURN)

        time.sleep(60)

        priceCraig = driverCraig.find_element(By.CLASS_NAME, "result-price")
        priceText = driver.find_element(By.CLASS_NAME, "pricing-price")

        # print(parsePrice(priceCraig.text))
        # print(parsePrice(priceText.text))
        out[parsePrice(priceCraig.text)] = driverCraig.current_url
        out[parsePrice(priceText.text)] = driver.current_url

        return process(out)
    except:
        print("Error")


def process(DictionaryValues):
    smallestPrice = sys.maxsize
    for eachPrice in DictionaryValues:
        if eachPrice < smallestPrice:
            smallestPrice = eachPrice


    return smallestPrice, DictionaryValues[smallestPrice]


def parsePrice(Price):
    price = ""
    for eachChar in Price:
        if eachChar == ".":
            break
        if eachChar != "$":
            price += eachChar
    return int(price)

# Code from Dev Ed YT for sending Email
def sendEmail(URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('mathew2002raj@gmail.com', 'authenticationPassword')

    subject = 'CheapestPrice!'
    body = f'check the Following Link: {URL}'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'mathew2002raj@gmail.com',
        'mathew2002raj@gmail.com',
        msg
    )
    print('Hey Email has been successfully sent')
    server.quit()
    return


#Main

CheapestPrice, CheapestURL = searchItem("Iphone 11")
print(CheapestPrice)
print(CheapestURL)
sendEmail(CheapestURL)

















