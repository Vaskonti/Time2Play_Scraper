import datetime

import requests
import sys

from bs4 import BeautifulSoup
import mail_service
from dotenv import dotenv_values

config = dotenv_values(".env")

if __name__ == "__main__":
    sys.stdout = open('games_sales.txt', 'a')
    response = requests.get("https://www.time2play.bg/")
    soup = BeautifulSoup(response.content, 'html.parser')

    title = None
    old_price = None
    new_price = None
    link = None
    imgSrc = None

    for row in soup.select('div.day-deal-holder'):
        title = row.find('div', class_='product-title').find('a').get_text()
        old_price = row.find('span', class_='old-price').get_text()
        new_price = row.find('span', class_='product-price').get_text()
        link = row.find('a', class_='product-image').get('href')
        imgSrc = row.find('img', class_='lazyload').get('data-src')
        print('Date:', datetime.datetime.now())
        print("Title: ", title)
        print("Old price: ", old_price)
        print("New price: ", new_price)
        print("Link: ", link)
        print("Image: ", imgSrc)
        print("---------------------------------------------------")

    template = mail_service.load_html_file("time2play.html")
    mail_service.send_email(
        "Time2Play.bg",
        template.render(title=title, old_price=old_price, new_price=new_price, link=link, date=datetime.datetime.now(),
                        image=imgSrc),
        config['RECEIVERS_TIME2PLAY'].split(","),
    )
