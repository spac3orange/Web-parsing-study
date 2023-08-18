import requests
import json
from bs4 import BeautifulSoup as bs

PATTERN_LINK = "https://parsinger.ru/html/"
URL = "https://parsinger.ru/html/index1_page_1.html"


def soup(link: str):
    request = requests.get(url=link)
    request.encoding = "utf-8"
    soup = bs(request.text, "lxml")
    return soup


all_categories = [PATTERN_LINK + i['href'] for i in soup(URL).find('div', class_='nav_menu').find_all('a')]
categories_names_list = [x['id'] for x in soup(URL).find('div', class_='nav_menu').find_all('div')]
all_page_links, all_items_links = [], []

for link in all_categories:
    pagen = [PATTERN_LINK + x['href'] for x in soup(link).find('div', class_='pagen').find_all('a')]
    all_page_links.append(pagen)
all_links = sum(all_page_links, [])

for link in all_links:
    all_items = [PATTERN_LINK + x['href'] for x in soup(link).find_all('a', class_='name_item')]
    all_items_links.append(all_items)
all_items_links = sum(all_items_links, [])
json_file = []

for url in all_items_links:
    product = soup(url)
    categorie = url.strip().split('/')[4]
    descr_tag = ''.join(product.find('div', class_='description')['class'])
    name = product.find('p', id='p_header')
    article = product.find('p', class_='article')
    article_tag = ''.join(product.find('p', class_='article')['class'])
    description = [x.text.strip().split('\n') for x in product.find('ul', id='description').find_all('li')]
    description = sum([[x.split(':')[1].strip() for x in sublist] for sublist in description], [])
    description_tags = [x['id'] for x in product.find('ul', id='description').find_all('li')]
    stock = product.find('span', id='in_stock')
    price = product.find('span', id='price')
    price_old = product.find('span', id='old_price')
    link = url

    json_file.append({
        'categorie': categorie,
        f'{name["id"]}': name.text,
        f"{article_tag}": article.text.split()[1],
        f"{descr_tag}": {

            f'{description_tags[0]}': description[0],
            f'{description_tags[1]}': description[1],
            f'{description_tags[2]}': description[2],
            f'{description_tags[3]}': description[3],
            f'{description_tags[4]}': description[4],
            f'{description_tags[5]}': description[5],
            f'{description_tags[6]}': description[6],
            f'{description_tags[7]}': description[7]
        },

        f'{stock["id"]}': stock.text.split(':')[1],
        f'{price["id"]}': price.text.split()[0],
        f'{price_old["id"]}': price_old.text.split()[0],
        'link': link

    })

with open('result3.json', 'w', encoding='utf-8') as file:
    json.dump(json_file, file, indent=4, ensure_ascii=False)

print('Запись завершена')