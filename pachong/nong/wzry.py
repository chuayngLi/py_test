import os.path
import requests
from lxml import etree
from time import sleep

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/120.0.0.0 Safari/537.36'}
hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
hero_list_resp = requests.get(hero_list_url, headers=headers)
# print(hero_list_resp.json())
# 实验两个
test = [
    hero_list_resp.json()[20]
]
for h in test:
    id_name = h.get('id_name')
    cname = h.get('cname')
    ename = h.get('ename')
    if not os.path.exists(cname):
        os.mkdir(cname)

    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{id_name}.shtml'
    hero_info_resp = requests.get(hero_info_url, headers=headers)
    hero_info_resp.encoding = 'gbk'
    e = etree.HTML(hero_info_resp.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')
    names = [name[0:name.index('&')] for name in names[0].split('|')]

    for i, n in enumerate(names):
        resp = requests.get(
            f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i + 1}.jpg',
            headers=headers)
        with open(f'{cname}/{n}.jpg', 'wb') as f:
            f.write(resp.content)
            print(f'已下载{n}皮肤')
            sleep(1)
