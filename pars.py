import requests
from bs4 import BeautifulSoup as bs


url = "https://kladr-rf.ru/"
file_out = open("adreses.txt", "w", encoding="utf-8")
for region in range(1, 100):
    if region < 10:
        region = "0" + str(region)
    r = requests.get(f"{url}{region}/")
    soup = bs(r.text, "html.parser")
    vacancies_names = soup.find_all('div')
    flag = False
    for data in vacancies_names:
        if flag:
            cities = data.find_all('li')
            for city in cities:
                if city.attrs.get("class", [None])[0] != "old" and city.attrs.get("class", [None])[0] != "del":
                    city_str = city.text
                    r = requests.get(f"{url}{city.a['href']}/")
                    soup = bs(r.text, "html.parser")
                    divs = soup.find_all('div')
                    flag = False
                    for div in divs:
                        if flag:
                            streets = div.find_all('li')
                            for street in streets:
                                if street.attrs.get("class", [None])[0] != "old" and \
                                        street.attrs.get("class", [None])[0] != "del":
                                    file_out.write(f"{city_str} {street.a.text}\n")
                            break
                        if div.text == 'Улицы':
                            flag = True
            break
        if data.text == 'Города':
            flag = True
file_out.close()
