import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36",
           "X-Amzn-Trace-Id": "Root=1-66805ca4-1e5b2b830d7be3560112eec4"}

def download(url):
    resp = requests.get(url, stream=True)
    r = open("C:\\Users\\123\\OneDrive\\Рабочий стол\\img\\" + url.split("/")[-1], "wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()

def get_url():


    for n in range(1, 8):
        sleep(1)
        url = f"https://scrapingclub.com/exercise/list_basic/?page={n}"

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.find_all("div", class_="w-full rounded border")

        for i in data:

            """name = i.find("h4").text
            price = i.find("h5").text
            url_img = 'https://scrapingclub.com' + i.find("img", class_="card-img-top img-fluid").get("src")
            print(name, price, url_img, sep="\n", end="\n\n")"""
            card_url = "https://scrapingclub.com" + i.find('a').get("href")
            yield card_url

def arr():
    for card in get_url():
        response_card = requests.get(card, headers=headers)

        sleep(1)

        soup_card = BeautifulSoup(response_card.text, 'html.parser')

        data_card = soup_card.find('div', class_='my-8 w-full rounded border')

        name = data_card.find("h3").text

        price = data_card.find("h4").text

        descr = data_card.find("p").text
        url_img = 'https://scrapingclub.com' + data_card.find("img", class_="card-img-top").get("src")
        download(url_img)

        yield name, price, descr, url_img