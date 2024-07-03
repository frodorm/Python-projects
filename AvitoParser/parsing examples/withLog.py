from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36",
           "X-Amzn-Trace-Id": "Root=1-66805ca4-1e5b2b830d7be3560112eec4"}

work = Session()

work.get("https://quotes.toscrape.com/", headers=headers)

response = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

token = soup.find("form").find("input").get("value")

data = {"csrf_token": token, "username": "noname", "password": "password"}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)

# количество страниц неопределено, когда останавливаться?
result = soup.find_all("span", class_="text")
author = soup.find_all("small", class_="author")

    if len(result) != 0:

    else:
        break