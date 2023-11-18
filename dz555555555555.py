import requests
from bs4 import BeautifulSoup

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