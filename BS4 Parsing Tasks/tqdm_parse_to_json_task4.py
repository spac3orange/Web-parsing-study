import json
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

url = 'https://parsinger.ru/html/index1_page_1.html'
shema = 'http://parsinger.ru/html/'

def get_soup(url):
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')         
    return soup

def get_nav_page(url):
    soup = get_soup(url)
    nav_page = soup.find('div', class_='nav_menu').find_all('a')
    nav_page = [f"{shema}{l['href']}" for l in nav_page]
    return nav_page

def get_pagen(url):
    soup = get_soup(url)
    pagen = soup.find('div', class_='pagen').find_all('a')
    pagen = [f"{shema}{l['href']}" for l in pagen]
    return pagen

def get_item_page(url):
    soup = get_soup(url)
    item_page = []
    item_page.extend([f'{shema}{href}' for href in [x['href'] for x in soup.find('div', class_='item_card').find_all('a', class_='name_item')]])
    return item_page

result_json = []

for url_np in get_nav_page(url):
    for url_p in tqdm(get_pagen(url_np), desc=f'Zapolnyaem kartochki iz {url_np}'):
        for item_url in get_item_page(url_p):
            soup = get_soup(item_url)
            dict_description = {x['id']: x.text.split(':')[1] for x in soup.find('ul', id='description').find_all('li')}
            merged_dict = {
                'categories': item_url.split('/')[4],
                'name': soup.find('p', id='p_header').text,
                'article': soup.find('p', class_='article').text.split(':')[1],
                'description': dict_description,
                'count': soup.find('span', id='in_stock').text.split(':')[1],
                'price': soup.find('span', id='price').text,
                'old_price': soup.find('span', id='old_price').text,
                'link': item_url
            }
            result_json.append(merged_dict)
with open('res.json', 'w', encoding='utf-8') as file:
    json.dump(result_json, file, indent=4, ensure_ascii=False)
    print(f'Fail {file} gotov \n Kol-vo tovarov = {len(result_json)}')