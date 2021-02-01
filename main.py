import send
from selenium import webdriver
from tinydb import TinyDB, Query
import config

db = TinyDB('OLXdb.json')

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r'chromedriver.exe', options=options)

driver.get("https://www.olx.pl/nieruchomosci/mieszkania/wynajem/rzeszow/?search%5Bfilter_float_price%3Ato%5D=700")

assert "Mieszkania" in driver.title

elem = driver.find_elements_by_class_name("offer-wrapper")

for e in elem:
    title = e.find_element_by_css_selector("strong").text
    url = e.find_element_by_class_name("link").get_attribute("href")
    price = e.find_element_by_css_selector(".price strong").text
    location = e.find_element_by_class_name("breadcrumb").text

    if db.search(Query()['url'] == url):
        print("Exist in db")

    else:
        print("Sending to Telegram")
        send.sendmessage(config.bot_api, config.chat_id, price + " " + location + url)
        db.insert({
            "url": url
        })

driver.close()
