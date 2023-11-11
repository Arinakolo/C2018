import requests
from bs4 import BeautifulSoup
import lxml
url = "https://rozetka.com.ua/mobile-phones/c80003/"
user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
header = {"User-Agent": user}
session = requests.Session()
response = session.get(url, headers=header)
print(response.status_code)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="lxml")

all_products = soup.find_all('li', class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
for product in all_products:
        product.find("div", class_="goods-title__old price--gray ng-star-interested")
        price=product.find("span", class_="goods-title__price-valee")
        title  =product.find("span", class_="goods-tile___title")
        print(price.text, title.text)

