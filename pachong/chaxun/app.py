# 手机号归属地查询

def get_mobile(phone):
    import requests
    from lxml import etree

    # 地址
    url = f'https://ip138.com/mobile.asp?mobile={phone}&action=mobile'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0.0.0 Safari/537.36'}
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    e = etree.HTML(resp.text)
    datas = e.xpath('//tr/td/a/text()')
    city = e.xpath('//tr[2]/td[2]/span/text()')
    if city:
        city = e.xpath('//tr[2]/td[2]/span/text()') + e.xpath('//tr[2]/td[2]/span/a/text()')
    else:
        city = e.xpath('//tr[2]/td[2]/span/a/text()')
    print('数据：', datas, '城市:', city)


get_mobile(18888888888)
