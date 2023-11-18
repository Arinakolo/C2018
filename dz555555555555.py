import requests
from bs4 import BeautifulSoup
import openpyxl

book = openpyxl.Workbook

count = 2
def chto_to(url):
    response = requests.get(url)
    soup =  BeautifulSoup(response.text,'html.parser')

    company_name = soup.find('h1', class_='campaign-name').text
    cashback_amount = soup.find('div', class_='cashback-amount').text


    with open('cashback_data.txt', 'a') as file:
        file.write(f'{company_name}: {cashback_amount}\n')


for page in range(1, 10):
    url = f'https://cash-backer.club/shops?page={page}'
    chto_to(url)



    sheet = book.active
    sheet['A1'] = "Title company"
    sheet['A1'] = "Procent cashback"
    book.save("Catalog.xlsx")

    book.close()