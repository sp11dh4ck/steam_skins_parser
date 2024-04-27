import requests
from bs4 import BeautifulSoup
import urllib
from config import s

url = f'https://wiki.cs.money/weapons/{s}'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

div_blocks = soup.find_all('div', class_='zhqwubnajobxbgkzlnptmjmgwn')
image_blocks = soup.find_all('img', class_='lnzmlhggcutlgtmffsmpefalne')

with open("skins.txt", "w", encoding="utf-8") as file:
    for div_block in div_blocks:
        file.write(div_block.text.strip() + "\n")

for i in range(len(image_blocks)):
    image_url = image_blocks[i]['src']
    if i % 2 != 0:
        urllib.request.urlretrieve(image_url, f'{s}/' + f"{i}.png")
    else:
        print("\033[32m{}".format(str(i) + " пропущен"))
