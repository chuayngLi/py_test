import requests
from lxml import etree

url = "https://nba.hupu.com/stats/players/pts"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36"}

# 发送请求
resp = requests.get(url, headers=headers)

# print(resp.text)
# 处理结果
# 解析响应请求
e = etree.HTML(resp.text)
nos = e.xpath('//table[@class="players_table"]//tr/td[1]/text()')
names = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
scores = e.xpath('//table[@class="players_table"]//tr/td[4]/text()')
# print(names)

with open('nba.txt', 'w', encoding='utf-8') as f:  # 创建或打开文件
    for no, name, teams, score in zip(nos, names, teams, scores):  # 遍历循环
        f.write(f'排名：{no} 姓名：{name} 球队：{teams} 得分：{score} \n')  # 写入文件
