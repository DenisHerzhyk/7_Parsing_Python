import requests
from bs4 import BeautifulSoup
from time import sleep

def get_url():
    for page in range(1, 7):
        link = f"https://scrapingclub.com/exercise/list_basic/?page={page}"

        response = requests.get(link).text
        soup = BeautifulSoup(response, 'lxml')
        block = soup.find_all('div', class_='w-full rounded border')

        for item in block:
            get_url = item.find("img", class_='card-img-top img-fluid').get("src")
            url_image = "https://scrapingclub.com/exercise/list_basic_detail/" + get_url[12:19] + "/"
            yield url_image

def get_product_info():
    for url in get_url():
        response = requests.get(url).text
        sleep(1)
        soup = BeautifulSoup(response, 'lxml')
        block = soup.find("div", class_="my-8 w-full rounded border")

        name = block.find('h3', class_='card-title').text
        price = block.find('h4', class_='my-4 card-price').text
        description = block.find('p', class_='card-description').text
        url_link = "https://scrapingclub.com" + block.find('img', class_='card-img-top').get('src')

        yield name, price, description, url_link