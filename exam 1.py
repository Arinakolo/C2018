import requests
from bs4 import BeautifulSoup
import pandas as pd


products_names = []
reviews_count = []
prices = []

discount_products_names = []
discount_reviews_count = []
discount_prices = []


for page_num in range(1, 25):
    url = f"https://allo.ua/ua/products/internet-planshety/?p={page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    products = soup.find_all("div", class_="product-item")
    for product in products:
        name = product.find("div", class_="product-title").text.strip()
        products_names.append(name)

        review_count = product.find("span", class_="review-count").text.strip()
        reviews_count.append(review_count)

        price = product.find("span", class_="price").text.strip()
        prices.append(price)

with open("products.txt", "w", encoding="utf-8") as file:
    for i in range(len(products_names)):
        file.write(f"Название: {products_names[i]}, Отзывы: {reviews_count[i]}, Цена: {prices[i]}\n")

data = {
    "Название": products_names,
    "Отзывы": reviews_count,
    "Цена": prices
}

df = pd.DataFrame(data)
df.to_excel("products.xlsx", index=False)




for page_num in range(1, 25):
    url = f"https://allo.ua/ua/products/internet-planshety/?p={page_num}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")


    discount_products = soup.find_all("div", class_="product-item sale")
    for product in discount_products:
        name = product.find("div", class_="product-title").text.strip()
        discount_products_names.append(name)

        review_count = product.find("span", class_="review-count").text.strip()
        discount_reviews_count.append(review_count)

        price = product.find("span", class_="price").text.strip()
        discount_prices.append(price)

with open("discount_products.txt", "w", encoding="utf-8") as file:
    for i in range(len(discount_products_names)):
        file.write(
            f"Название: {discount_products_names[i]}, Отзывы: {discount_reviews_count[i]}, Цена: {discount_prices[i]}\n")

data = {
    "Название": discount_products_names,
    "Отзывы": discount_reviews_count,
    "Цена": discount_prices
}

df = pd.DataFrame(data)
df.to_excel("discount_products.xlsx", index=False)