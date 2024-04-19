from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# 登录
@app.route('/login')
def login():
    account = request.args.get('account')
    password = request.args.get('password')
    if account == 'admin' and password == '123456':
        return '<h1>登录成功</h1>'
    else:
        return '<h1>账号密码错误</h1>' \
               '<a href="/">重新登录</a>'


app.run(debug=True)
