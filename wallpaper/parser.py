import requests
from bs4 import BeautifulSoup as bs

def image_parser(param_image:str):
    content = param_image.split(" ")[1::]
    url = f"https://wallpaperscraft.ru/search/?order=&page=1&query={''.join(str(word) for word in content)}&size=1920x1080"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    response = requests.get(url, headers=headers)
    html = response.content

    soup = bs(html, 'html.parser')
    img_tags = soup.find_all('img')
    img_urls = []
    for img in img_tags:
        img_url = img.get('src')
        if img_url and ('.png' or '.jpg' or '.jpeg' in img_url):
            img_urls.append(img_url)
    return img_urls[1:5]