import requests
from time import sleep
from lxml import etree

url = 'https://desk.3gbizhi.com/deskMV/index_6.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 '
                  'Safari/537.36'
}

resp = requests.get(url, headers=headers)
resp.encoding = 'utf-8'
e = etree.HTML(resp.text)

img_urls = e.xpath("//li[@class='box_black']/a/img/@lay-src")
img_names = e.xpath("//li[@class='box_black']/a/img/@alt")

for u, n in zip(img_urls, img_names):
    print(f'图片名：{n}正在下载')
    img_resp = requests.get(u, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'
    })
    with open(f'./images/{n}.jpg', 'wb') as f:
        f.write(img_resp.content)
    sleep(1)
