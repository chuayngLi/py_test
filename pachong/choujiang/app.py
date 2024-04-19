# 支持服务访问
# 需要一个web框架
# pip install Flask
from random import randint

from flask import Flask, render_template

app = Flask(__name__)

hero = [
    '机械先驱', '北地之怒 ', '无双剑姬', '爆破鬼才', '仙灵女巫', '生化魔人',
    '疾风剑豪', '虚空之眼', '岩雀', '青钢影', '影哨', '虚空女皇', '弗雷尔卓德之心',
    '戏命师'
]


@app.route('/index')  # 路由
def index():
    return render_template('index.html', hero=hero)  # 页面显示


@app.route('/choujiang')
def choujiang():
    num = randint(0, len(hero) - 1)
    return render_template('index.html', hero=hero, h=hero[num])


app.run(debug=True)
