import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import json
from datetime import datetime
from DB.realty import check_database

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36",
           "X-Amzn-Trace-Id": "Root=1-66805ca4-1e5b2b830d7be3560112eec4"}

def get_json(url):

    data = {}

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')

    scripts = soup.find_all('script')

    for script in scripts:

        if 'window.__initialData__' in script.text:

            jsonText = script.text.split(';')[0].split('=')[-1].strip()

            jsonText = unquote(jsonText)

            jsonText = jsonText[1:-1]

            data = json.loads(jsonText)
            """try:
                            with open('data.json', 'w', encoding='utf-8') as file:
        
                                json.dump(data, file, ensure_ascii=False)
        
                            print("Файл успешно создан.")
        
                        except Exception as e:
        
                            print(f"Произошла ошибка: {e}")"""
    return data

def get_offers(data):

    offers = []

    for key in data:

        if 'single-page' in key:

            items = data[key]["data"]["catalog"]["items"]

            for item in items:

                if item.get("id"):

                    offer = {}

                    parts = item["title"].split(', ')

                    parts = [part.replace('\xa0', ' ').strip() for part in parts]

                    offer["title"] = parts[0]
                    offer["url"] = "https://www.avito.ru" + item["urlPath"]
                    offer["offer_id"] = item["id"]


                    timeStamp = datetime.fromtimestamp(item["sortTimeStamp"] / 1000)

                    timeStamp = datetime.strftime(timeStamp, '%d.%m.%Y в %H:%M')

                    offer["date"] = timeStamp

                    offer["price"] = item["priceDetailed"]["value"]

                    if "geo" in item and "geoReferences" in item["geo"] and len(item["geo"]["geoReferences"]) > 0:

                        city = item["geo"]["geoReferences"][0]["content"]

                    else:

                        city = "Калининградская область"

                    address = item["geo"]["formattedAddress"]

                    offer["address"] = city + ', ' + address
                    offer["area"] = parts[1]
                    offer["floor"] = parts[2]


                    offers.append(offer)

    return offers

def main():

    url = f"https://www.avito.ru/kaliningrad/kvartiry/prodam-ASgBAgICAUSSA8YQ?context=H4sIAAAAAAAA_0q0MrSqLraysFJKK8rPDUhMT1WyLrYyt1JKTixJzMlPV7KuBQQAAP__dhSE3CMAAAA&f=ASgBAgICAkSSA8YQkL4Nlq41&s=104"

    data = get_json(url)

    offers = get_offers(data)

    for offer in offers:
        check_database(offer)


main()